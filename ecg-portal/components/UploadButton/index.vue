<template>
  <div class="upload-container">
    <el-upload
      :class="className"
      :on-preview="handlePreview"
      :on-remove="handleRemove"
      action="/upload"
      :before-remove="beforeRemove"
      :limit="1"
      :file-list="fileList"
      :on-success="handleSuccess"
      :on-error="handleError"
    >
      <el-button
        class="upload-btn"
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
    <el-button class="submit-btn" type="primary" @click="submitUpload"
      >Submit</el-button
    >
  </div>
</template>

<script>
export default {
  data() {
    return {
      fileList: [],
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
    beforeRemove(file, fileList) {
      return this.$confirm(`Cancel the transfert of ${file.name} ?`)
    },
    emitClickEvent() {
      this.$emit('click')
    },
    handleSuccess(response, file, fileList) {
      // Handle successful upload
    },
    handleError(error, file, fileList) {
      // Handle failed upload
    },
    submitUpload() {
      console.log('Submit')
    },
  },
}
</script>

<style lang="scss" scoped>
.upload-container {
  display: flex;
  justify-content: space-between;
  width: 50%;

  .upload-btn {
    height: 40px;
  }

  .submit-btn {
    height: 40px;
  }
}
</style>