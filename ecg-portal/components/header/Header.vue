<template>
  <nav
    class="flex justify-between sticky top-0 bg-white z-10 shadow-md"
    role="navigation"
    aria-label="main navigation"
  >
    <nuxt-link
      :to="{ name: 'index' }"
      class="app-logo navbar-item flex items-center"
    >
      <h1 class="title w-20 h-12"></h1>
      <span>ECG Portal</span>
    </nuxt-link>

    <div class="flex items-center hospital-container">
      <nuxt-link :to="{ name: 'about-ecg' }" class="about flex items-center">
        <div class="icon-ecg w-20 h-12"></div>
        <span>About ECG</span>
      </nuxt-link>

      <nuxt-link
        :to="{ name: 'analyze-ecg' }"
        class="analyse flex items-center"
      >
        <div class="icon-ecg w-20 h-12"></div>
        <span>Analyze ECG</span>
      </nuxt-link>

      <nuxt-link
        v-for="(hospital, id) in HOSPITAL_CONFIG"
        :to="{ name: 'hospital-id', params: { id: hospital.id } }"
        class="hospital flex items-center"
        :key="id"
      >
        <div class="icon-hospital w-20 h-12"></div>
        <span>{{ hospital.name }}</span>
      </nuxt-link>
    </div>
  </nav>
</template>

<script>
import { HOSPITAL_CONFIG } from '@/constants'
export default {
  name: 'VmHeader',

  data() {
    return {
      HOSPITAL_CONFIG,
    }
  },

  computed: {},

  mounted() {},
  destroyed() {},

  methods: {},
}
</script>

<style lang="scss" scoped>
.app-logo {
  padding: 16px;
}

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

  .about {
    padding: 16px;

    .icon-ecg {
      background: url('../../static/info-icon.png') no-repeat;
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
