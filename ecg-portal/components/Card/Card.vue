<template>
  <el-card :class="classnames('box-card', className)">
    <h1 class="title">{{ title }}</h1>

    {{ cardContent }}
  </el-card>
</template>

<script>
import classnames from 'classnames'

export default {
  name: 'CardComponent',
  props: {
    title: {
      type: String,
      default: '',
    },
    cardContent: {
      type: String,
      default: '',
    },
    className: {
      type: String,
      default: '',
    },
  },
  methods: {
    classnames,
  },
}
</script>

<style lang="scss" scoped>
.text {
  font-size: 14px;
}

.item {
  padding: 18px 0;
}

.box-card {
  width: 480px;
  padding: 14px;

  .title {
    margin-bottom: 16px;
    font-weight: 600;
  }
}
</style>