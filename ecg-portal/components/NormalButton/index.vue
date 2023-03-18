<template>
  <el-button :type="type" :size="size">{{ buttonName }}</el-button>
</template>

<script>
export default {
  name: 'NormalButton',
  props: {
    buttonName: {
      type: String,
      default: '',
    },
    type: {
      type: String,
      default: 'primary',
    },
    size: {
      type: String,
      default: 'medium',
    },
  },
}
</script>

<style>
</style>