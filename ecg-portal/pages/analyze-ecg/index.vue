<template>
  <div class="analyze-page">
    <sidebar />
    <div class="analyze-page__main">
      <div class="title">ECG Report</div>

      <div v-if="isEmpty(hospitalData.ecgResult)" class="image-container">
        <img
          src="@/static/images/analyze-pic.jpg"
          alt="No data image"
          width="700px"
          class="no-data-image"
        />
      </div>

      <ecg-details
        v-else
        class="info-container"
        extendedText="Swarm Learning"
        :ecgResult="hospitalData.ecgResult"
        :hospitalId="hospitalId"
        :isShowViewMore="isShowViewMore"
      />

      <div class="button-container">
        <upload-button
          v-if="isEmpty(hospitalData.ecgResult)"
          button-name="Click to upload"
          upload-tip="Please provide ECG data (.asc format)"
          className="upload-btn"
          buttonClass="custom-btn"
          @click="handleUploadEcgDataRaw"
        />

        <normal-button
          v-else
          button-name="Delete"
          className="delete-btn"
          @click="handleDeleteEcgDataRaw"
        />
      </div>
    </div>
  </div>
</template>

<script>
import Sidebar from '@/components/Sidebar'
import UploadButton from '@/components/UploadButton'
import NormalButton from '@/components/NormalButton'
import EcgDetails from '@/components/EcgDetails'
import { isEmpty } from 'lodash'

export default {
  name: 'Analyze-ECG-page',
  components: {
    Sidebar,
    UploadButton,
    NormalButton,
    EcgDetails,
  },
  data() {
    return {
      hospitalData: {},
      hospitalId: 0,
      isShowViewMore: true,
    }
  },
  mounted() {
    this.hospitalData = this.$store.getters.getHospitalById(0)
  },
  methods: {
    isEmpty,
    handleUploadEcgDataRaw() {
      // ! Handle raw data from .asc file

      this.$store.commit('setEcgDataRaw', '263 882 533 925 824 252 95')

      // ! testing after recieving the result from API request

      const resultList = [
        {
          title: 'Normal ECG',
          value: '70',
        },
        {
          title: 'Abnormal ECG',
          value: '5',
        },
        {
          title: 'Borderline ECG',
          value: '2',
        },
        {
          title: 'Otherwise normal ECG',
          value: '23',
        },
      ]

      const newResultList = resultList.map((item) => ({
        title: item.title,
        value: item.value,
        additionalClass: 'bold',
        unit: '%',
      }))

      this.$store.commit('setEcgResult', {
        id: 0,
        ...newResultList,
      })
    },
    handleDeleteEcgDataRaw() {
      this.$store.commit('setEcgDataRaw', '')

      this.$store.commit('resetEcgResult', 0)
    },
  },
}
</script>

<style lang="scss" scoped>
.analyze-page {
  min-height: calc(100vh - $header-height - $header-height);
  display: flex;
  justify-content: center;

  &__main {
    width: 100%;

    .title {
      margin-top: 36px;
      font-size: 24px;
      text-align: center;
    }

    .image-container,
    .info-container {
      margin-top: 32px;
      padding-bottom: 48px;
      display: flex;
      justify-content: center;
    }

    .button-container {
      display: flex;
      width: 100%;

      padding-left: 48px;
      padding-bottom: 48px;

      .upload-btn {
        height: 40px;
      }

      .custom-btn {
        height: 40px;
      }

      .delete-btn {
        height: 40px;
      }
    }
  }
}
</style>