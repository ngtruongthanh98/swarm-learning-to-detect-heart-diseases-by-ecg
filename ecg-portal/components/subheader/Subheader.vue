<template>
  <div class="subheader-wrapper m-4 p-4 text-center">
    <ecg-viewer />
  </div>
</template>

<script>
import EcgViewer from '../EcgViewer/EcgViewer'

export default {
  name: 'VmSubheader',

  components: {
    EcgViewer,
  },
}
</script>

<style lang="scss" scoped>
.subheader-wrapper {
  min-height: calc(100vh - 80px - 300px - 80px - 32px);

  display: flex;
  align-items: center;
}
</style>
