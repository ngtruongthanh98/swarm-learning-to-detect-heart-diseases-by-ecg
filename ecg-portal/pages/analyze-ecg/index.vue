<template>
  <div class="analyze-page">
    <sidebar />
    <div class="analyze-page__main">
      <h1 class="title">Analyze page</h1>
    </div>
  </div>
</template>

<script>
import Sidebar from '@/components/Sidebar'
export default {
  name: 'Analyze-ECG-page',
  components: {
    Sidebar,
  },
}
</script>

<style lang="scss" scoped>
.analyze-page {
  min-height: calc(100vh - 80px - 80px);

  display: flex;
  // justify-content: center;

  &__main {
    .title {
      margin-top: 36px;
      font-size: 24px;
    }
  }
}
</style>