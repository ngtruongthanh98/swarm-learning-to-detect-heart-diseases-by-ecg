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
        const response = await this.$axios.get(`/api/result/${this.hospitalId}`)
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
      } else {
        // Swarm Learning
        for (let id = 0; id < 6; id++) {
          const response = await this.$axios.get(`/api/result/${id}`)
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
        }

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
