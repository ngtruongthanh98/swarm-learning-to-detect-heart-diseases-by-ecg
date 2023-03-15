<template>
  <div class="hospital-page">
    <div class="title">{{ hospitalName }}</div>
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
  justify-content: center;

  .title {
    margin-top: 36px;
  }
}
</style>

