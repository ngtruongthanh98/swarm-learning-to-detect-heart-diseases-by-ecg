<template>
  <div class="upload-container">
    <el-upload
      :class="className"
      :on-preview="handlePreview"
      :on-remove="handleRemove"
      action="/upload"
      :before-remove="beforeRemove"
      :limit="1"
      :file-list="fileList"
      :on-success="handleSuccess"
      :on-error="handleError"
    >
      <el-button
        class="upload-btn"
        :class="buttonClass"
        :size="size"
        type="primary"
        @click="emitClickEvent"
        >{{ buttonName }}</el-button
      >
      <div slot="tip" class="el-upload__tip">
        {{ uploadTip }}
      </div>
    </el-upload>
    <el-button class="submit-btn" type="primary" @click="submitUpload"
      >Submit</el-button
    >
  </div>
</template>

<script>
import { isEmpty } from 'lodash'

export default {
  data() {
    return {
      fileList: [],
    }
  },
  props: {
    buttonName: {
      type: String,
      default: '',
    },
    uploadTip: {
      type: String,
      default: '',
    },
    className: {
      type: String,
      default: '',
    },
    size: {
      type: String,
      default: '',
    },
    buttonClass: {
      type: String,
      default: '',
    },
    hospitalId: {
      type: Number,
      required: true,
    },
    isSingleHospital: {
      type: Boolean,
      required: true,
    },
  },
  methods: {
    handleRemove(file, fileList) {
      console.log(file, fileList)
    },
    handlePreview(file) {
      console.log(file)
    },
    beforeRemove(file, fileList) {
      return this.$confirm(`Cancel the transfert of ${file.name} ?`)
    },
    emitClickEvent() {
      this.$emit('click')
    },
    handleSuccess(response, file, fileList) {
      // Handle successful upload
      const reader = new FileReader()
      reader.readAsText(file.raw)
      reader.onload = () => {
        const fileData = reader.result

        this.fileData = fileData
        this.fileName = file.raw.name

        const numbersArray = fileData
          .split('\n')
          .flatMap((row) => row.split(' ').map(Number))

        this.$store.commit('setEcgDataRaw', numbersArray)
      }
    },
    handleError(error, file, fileList) {
      // Handle failed upload
    },
    async submitUpload() {
      console.log('Submited')

      if (isEmpty(this.$store.state.ecgDataRaw)) {
        return
      }

      if (this.isSingleHospital) {
        if (this.hospitalId === 1 || this.hospitalId === 2) {
          const response = await this.$axios.post(
            `http://127.0.0.1:5000/result/cnn/${this.hospitalId}`,
            {
              body: {
                data: this.fileData,
              },
              headers: {
                'Content-Type': 'application/json',
              },
            }
          )

          const resultList = response.data
          const newResultList = resultList?.map((item) => ({
            title: item.title,
            value: item.value,
            additionalClass: 'bold',
            unit: '%',
          }))
          this.$store.commit('setEcgResult', {
            id: this.hospitalId,
            result: newResultList,
          })
        }

        if (
          this.hospitalId === 3 ||
          this.hospitalId === 4 ||
          this.hospitalId === 5
        ) {
          const response = await this.$axios.post(
            `http://127.0.0.1:5000/result/svm/${this.hospitalId}`,
            {
              body: {
                data: this.fileName,
              },
              headers: {
                'Content-Type': 'application/json',
              },
            }
          )

          const resultList = response.data
          const newResultList = resultList?.map((item) => ({
            title: item.title,
            value: item.value,
            additionalClass: 'bold',
            unit: '%',
          }))
          this.$store.commit('setEcgResult', {
            id: this.hospitalId,
            result: newResultList,
          })
        }
      } else {
        // Swarm Learning
        // Using CNN Model
        for (let id = 1; id < 3; id++) {
          const response = await this.$axios.post(
            `http://127.0.0.1:5000/result/cnn/${id}`,
            {
              body: {
                data: this.fileData,
              },
              headers: {
                'Content-Type': 'application/json',
              },
            }
          )

          const resultList = response.data
          const newResultList = resultList?.map((item) => ({
            title: item.title,
            value: item.value,
            additionalClass: 'bold',
            unit: '%',
          }))
          this.$store.commit('setEcgResult', {
            id: id,
            result: newResultList,
          })

          if (id === 1) {
            this.valuesArray1 = resultList.map((item) => item.value)
          }

          if (id === 2) {
            this.valuesArray2 = resultList.map((item) => item.value)
          }

          // if (id === 3) {
          //   this.valuesArray3 = resultList.map((item) => item.value)
          // }

          // if (id === 4) {
          //   this.valuesArray4 = resultList.map((item) => item.value)
          // }

          // if (id === 5) {
          //   this.valuesArray5 = resultList.map((item) => item.value)
          // }
        }

        // Using SVM Model
        for (let id = 3; id < 6; id++) {
          const response = await this.$axios.post(
            `http://127.0.0.1:5000/result/svm/${id}`,
            {
              body: {
                data: this.fileName,
              },
              headers: {
                'Content-Type': 'application/json',
              },
            }
          )

          const resultList = response.data
          const newResultList = resultList?.map((item) => ({
            title: item.title,
            value: item.value,
            additionalClass: 'bold',
            unit: '%',
          }))
          this.$store.commit('setEcgResult', {
            id: id,
            result: newResultList,
          })

          if (id === 3) {
            this.valuesArray3 = resultList.map((item) => item.value)
          }

          if (id === 4) {
            this.valuesArray4 = resultList.map((item) => item.value)
          }

          if (id === 5) {
            this.valuesArray5 = resultList.map((item) => item.value)
          }
        }

        // Define the column order
        const columnOrder = [
          'Normal ECG',
          'Abnormal ECG',
          'Otherwise normal ECG',
          'Borderline ECG',
        ]

        // Create the sumArray with values added
        const sumArray = this.valuesArray1.map((item, index) => ({
          value:
            this.valuesArray1[index] +
            this.valuesArray2[index] +
            this.valuesArray3[index] +
            this.valuesArray4[index] +
            this.valuesArray5[index],
        }))

        // Add the column order to each item in the sumArray
        const sumArrayWithOrder = sumArray.map((item, index) => ({
          title: columnOrder[index],
          value: item.value,
        }))

        // Calculate the sum of all values in the sumArray
        const sumOfValues = sumArrayWithOrder.reduce(
          (acc, item) => acc + item.value,
          0
        )

        // Calculate the percentage of each value in the sumArrayWithOrder
        const sumArrayWithPercentage = sumArrayWithOrder.map((item) => ({
          title: item.title,
          value: ((item.value / sumOfValues) * 100).toFixed(2),
          additionalClass: 'bold',
          unit: '%',
        }))

        this.$store.commit('setEcgResult', {
          id: 0,
          result: sumArrayWithPercentage,
        })

        this.$store.commit('setIsSwarmLearningDone', true)
      }
    },
  },
}
</script>

<style lang="scss" scoped>
.upload-container {
  display: flex;
  justify-content: space-between;
  width: 50%;

  .upload-btn {
    height: 40px;
  }

  .submit-btn {
    height: 40px;
  }
}
</style>
