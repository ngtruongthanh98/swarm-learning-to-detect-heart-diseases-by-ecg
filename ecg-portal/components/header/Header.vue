<template>
  <nav
    class="flex justify-between sticky top-0 bg-white z-10 shadow-md"
    role="navigation"
    aria-label="main navigation"
  >
    <nuxt-link :to="{ name: 'index' }" class="navbar-item flex items-center">
      <h1 class="title w-20 h-12"></h1>
      <span>ECG Portal</span>
    </nuxt-link>

    <div class="flex items-center hospital-container">
      <div class="analyse flex items-center">
        <div class="icon-ecg w-20 h-12"></div>
        <span>ECG Analyse</span>
      </div>

      <div class="hospital flex items-center">
        <div class="icon-hospital w-20 h-12"></div>
        <span>Cho Ray Hospital</span>
      </div>

      <div class="hospital flex items-center">
        <div class="icon-hospital w-20 h-12"></div>
        <span>Bach Mai Hospital</span>
      </div>

      <div class="hospital flex items-center">
        <div class="icon-hospital w-20 h-12"></div>
        <span>Tam Duc Hospital</span>
      </div>

      <div class="hospital flex items-center">
        <div class="icon-hospital w-20 h-12"></div>
        <span>Viet Phap Hospital</span>
      </div>

      <div class="hospital flex items-center">
        <div class="icon-hospital w-20 h-12"></div>
        <span>115 Hospital</span>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: 'VmHeader',

  data() {
    return {}
  },

  computed: {},

  mounted() {},
  destroyed() {},

  methods: {},
}
</script>

<style lang="scss" scoped>
.title {
  background: url('../../static/heart-logo.png') no-repeat;
  background-position: 50% 50%;
  background-size: 40px;
}

.hospital-container {
  .hospital {
    padding: 16px;

    .icon-hospital {
      background: url('../../static/hospital-icon.png') no-repeat;
      background-position: 50% 50%;
      background-size: 40px;
    }

    &:hover {
      cursor: pointer;
      background-color: $primary-third;
    }
  }

  .analyse {
    padding: 16px;

    .icon-ecg {
      background: url('../../static/ecg-icon.png') no-repeat;
      background-position: 50% 50%;
      background-size: 40px;
    }

    &:hover {
      cursor: pointer;
      background-color: $primary-inverted;
    }
  }
}
</style>
