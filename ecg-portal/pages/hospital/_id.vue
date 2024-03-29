<template>
  <div class="hospital-page">
    <sidebar />
    <div class="hospital-page__main">
      <h1 class="title">
        {{ hospitalName }}
        <span
          ><img
            :src="hospitalLogoPath"
            alt="Logo"
            width="128"
            height="128"
            class="logo"
        /></span>
      </h1>

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
        :extendedText="hospitalName"
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
          :hospitalId="hospitalId"
          :isSingleHospital="isSingleHospital"
          @click="handleUploadEcgDataRaw"
        />

        <normal-button
          v-else
          button-name="Clear the report"
          className="delete-btn"
          @click="handleDeleteEcgDataRaw"
        />
      </div>
    </div>
  </div>
</template>

<script>
import { HOSPITAL_CONFIG } from '@/constants'
import Sidebar from '@/components/Sidebar'
import UploadButton from '@/components/UploadButton'
import NormalButton from '@/components/NormalButton'
import EcgDetails from '@/components/EcgDetails'
import { isEmpty } from 'lodash'

export default {
  name: 'hospital-id',

  components: {
    Sidebar,
    UploadButton,
    NormalButton,
    EcgDetails,
  },

  validate({ params }) {
    return /^\d+$/.test(params.id)
  },

  data() {
    return {
      hospitalId: 0,
      hospitalData: {},
      isShowViewMore: false,
      hospitals: HOSPITAL_CONFIG,
      isSingleHospital: true,
    }
  },
  computed: {
    hospitalName() {
      const hospital = this.hospitals.find((h) => h.id === this.hospitalId)
      return hospital ? hospital.name : 'Unknown Hospital'
    },
    hospitalLogoPath() {
      const hospital = this.hospitals.find((h) => h.id === this.hospitalId)
      return hospital ? hospital.logoPath : ''
    },
  },

  mounted() {
    this.hospitalId = Number(this.$route.params.id)
    this.hospitalData = this.$store.getters.getHospitalById(
      this.$route.params.id
    )
  },
  methods: {
    isEmpty,
    handleUploadEcgDataRaw() {
      // ! Handle raw data from .asc file
      this.hospitalData = this.$store.getters.getHospitalById(
        this.$route.params.id
      )

      this.$store.commit('resetEcgResult', this.$route.params.id)
    },
    handleDeleteEcgDataRaw() {
      this.$store.commit('setEcgDataRaw', [])

      this.$store.commit('resetEcgResult', this.$route.params.id)
    },
  },
}
</script>

<style lang="scss" scoped>
.hospital-page {
  min-height: calc(100vh - $header-height - $header-height);

  display: flex;

  &__main {
    width: 100%;

    .title {
      margin-top: 36px;
      font-size: 24px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;

      .logo {
        margin-top: 5px;
      }
    }

    .hospital-logo {
      height: 150px;
      width: 150px;
      margin-top: 16px;
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
      justify-content: center;
      width: 100%;

      padding-left: 48px;
      padding-right: 48px;
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
