<template>
  <div class="analyze-page">
    <sidebar />
    <div class="analyze-page__main">
      <div class="title">ECG Report</div>

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
import Sidebar from '@/components/Sidebar'
import UploadButton from '@/components/UploadButton'
import NormalButton from '@/components/NormalButton'
import EcgDetails from '@/components/EcgDetails'

export default {
  name: 'Analyze-ECG-page',
  components: {
    Sidebar,
    UploadButton,
    NormalButton,
    EcgDetails,
  },
  methods: {
    handleUploadEcgDataRaw() {
      this.$store.commit('setEcgDataRaw', '263 882 533 925 824 252 95')
    },
    handleDeleteEcgDataRaw() {
      this.$store.commit('setEcgDataRaw', '')
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