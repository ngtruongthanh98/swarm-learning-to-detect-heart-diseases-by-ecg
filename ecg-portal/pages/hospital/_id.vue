<template>
  <div class="hospital-page">
    <div class="title">{{ hospitalName }}</div>
    <img :src="hospitalLogo" alt="hospital logo" class="hospital-logo" />
  </div>
</template>

<script>
import { HOSPITAL_CONFIG } from '@/constants'

export default {
  name: 'hospital-id',

  components: {},

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

    console.log('hospitalId: ', this.hospitalId)
  },
}
</script>

<style lang="scss" scoped>
.hospital-page {
  min-height: calc(100vh - 80px - 80px);

  display: flex;
  flex-direction: column;
  align-items: center;

  .title {
    margin-top: 36px;
    font-size: 24px;
  }

  .hospital-logo {
    height: 150px;
    width: 150px;
    margin-top: 16px;
  }
}
</style>

