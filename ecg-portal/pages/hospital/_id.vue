<template>
  <div class="hospital-page">
    <sidebar />
    <div class="hospital-page__main">
      <h1 class="title">{{ hospitalName }}</h1>
    </div>
  </div>
</template>

<script>
import { HOSPITAL_CONFIG } from '@/constants'
import Sidebar from '@/components/Sidebar'

export default {
  name: 'hospital-id',

  components: {
    Sidebar,
  },

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
  },
}
</script>

<style lang="scss" scoped>
.hospital-page {
  min-height: calc(100vh - $header-height - $header-height);

  display: flex;

  &__main {
    width: 100%;
    background-color: pink;

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
}
</style>

