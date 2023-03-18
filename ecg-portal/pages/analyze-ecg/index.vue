<template>
  <div class="analyze-page">
    <sidebar />
    <div class="analyze-page__main">
      <div class="title">ECG report</div>

      <div class="button-container">
        <upload-button
          button-name="Click to upload"
          upload-tip="Please provide ECG data (.asc format)"
        />
        <normal-button button-name="Delete" />
      </div>
    </div>
  </div>
</template>

<script>
import Sidebar from '@/components/Sidebar'
import UploadButton from '@/components/UploadButton'
import NormalButton from '@/components/NormalButton'

export default {
  name: 'Analyze-ECG-page',
  components: {
    Sidebar,
    UploadButton,
    NormalButton,
  },
}
</script>

<style lang="scss" scoped>
.analyze-page {
  min-height: calc(100vh - $header-height - $header-height);
  display: flex;

  &__main {
    width: 100%;

    .title {
      margin-top: 36px;
      font-size: 24px;
      text-align: center;
    }

    .button-container {
    }
  }
}
</style>