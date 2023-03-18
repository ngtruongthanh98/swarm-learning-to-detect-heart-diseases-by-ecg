<template>
  <el-button :type="type" :size="size" :class="className">{{
    buttonName
  }}</el-button>
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
      default: '',
    },
    className: {
      type: String,
      default: '',
    },
  },
}
</script>

<style>
</style>