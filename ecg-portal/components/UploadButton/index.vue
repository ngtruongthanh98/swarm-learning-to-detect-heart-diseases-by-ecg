<template>
  <el-upload
    :class="className"
    action="https://jsonplaceholder.typicode.com/posts/"
    :on-preview="handlePreview"
    :on-remove="handleRemove"
    :before-remove="beforeRemove"
    multiple
    :limit="3"
    :on-exceed="handleExceed"
    :file-list="fileList"
  >
    <el-button
      :class="buttonClass"
      :size="size"
      type="primary"
      @click="emitClickEvent"
      >{{ buttonName }}</el-button
    >
    <div slot="tip" class="el-upload__tip">
      {{ uploadTip }}
    </div>
  </el-upload>
</template>

<script>
export default {
  data() {
    return {
      fileList: [
        // {
        //   name: 'food.jpeg',
        //   url: 'https://fuss10.elemecdn.com/3/63/4e7f3a15429bfda99bce42a18cdd1jpeg.jpeg?imageMogr2/thumbnail/360x360/format/webp/quality/100',
        // },
        // {
        //   name: 'food2.jpeg',
        //   url: 'https://fuss10.elemecdn.com/3/63/4e7f3a15429bfda99bce42a18cdd1jpeg.jpeg?imageMogr2/thumbnail/360x360/format/webp/quality/100',
        // },
      ],
    }
  },
  props: {
    buttonName: {
      type: String,
      default: '',
    },
    uploadTip: {
      type: String,
      default: '',
    },
    className: {
      type: String,
      default: '',
    },
    size: {
      type: String,
      default: '',
    },
    buttonClass: {
      type: String,
      default: '',
    },
  },
  methods: {
    handleRemove(file, fileList) {
      console.log(file, fileList)
    },
    handlePreview(file) {
      console.log(file)
    },
    handleExceed(files, fileList) {
      this.$message.warning(
        `The limit is 3, you selected ${
          files.length
        } files this time, add up to ${files.length + fileList.length} totally`
      )
    },
    beforeRemove(file, fileList) {
      return this.$confirm(`Cancel the transfert of ${file.name} ?`)
    },
    emitClickEvent() {
      this.$emit('click')
    },
  },
}
</script>

<style lang="scss" scoped>
</style>