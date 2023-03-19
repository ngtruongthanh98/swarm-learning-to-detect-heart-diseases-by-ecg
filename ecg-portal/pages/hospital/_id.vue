<template>
  <div class="hospital-page">
    <sidebar />
    <div class="hospital-page__main">
      <h1 class="title">{{ hospitalName }}</h1>

      <div v-if="!this.$store.state.ecgDataRaw" class="image-container">
        <img
          src="@/static/images/analyze-pic.jpg"
          alt="No data image"
          width="800px"
          class="no-data-image"
        />
      </div>

      <ecg-details v-else class="info-container" />

      <div class="button-container">
        <upload-button
          v-if="!this.$store.state.ecgDataRaw"
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
import { HOSPITAL_CONFIG } from '@/constants'
import Sidebar from '@/components/Sidebar'
import UploadButton from '@/components/UploadButton'
import NormalButton from '@/components/NormalButton'
import EcgDetails from '@/components/EcgDetails'

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
      hospitalId: '',
      hospitals: HOSPITAL_CONFIG,
    }
  },
  computed: {
    hospitalName() {
      const hospital = this.hospitals.find((h) => h.id === this.hospitalId)
      return hospital ? hospital.name : 'Unknown Hospital'
    },
    hospitalLogo() {
      const hospital = this.hospitals.find((h) => h.id === this.hospitalId)
      return hospital ? hospital.logoPath : ''
    },
  },

  mounted() {
    this.hospitalId = this.$route.params.id
  },
  methods: {
    handleUploadEcgDataRaw() {
      this.$store.commit('setEcgDataRaw', '263 882 533 925 824 252 95')

      // ! testing after recieving the result from API request

      const ecgResult = {
        normalEcg: '20',
        abnormalEcg: '20',
        borderlineEcg: '20',
        OtherwiseNormalEcg: '40',
      }

      this.$store.commit('setEcgResult', {
        id: this.hospitalId,
        ...ecgResult,
      })
    },
    handleDeleteEcgDataRaw() {
      this.$store.commit('setEcgDataRaw', '')
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
      text-align: center;
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

