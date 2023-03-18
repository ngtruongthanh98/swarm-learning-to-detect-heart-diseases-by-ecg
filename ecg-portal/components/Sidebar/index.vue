<template>
  <div class="sidebar">
    <div class="sidebar__container">
      <nuxt-link
        :to="{ name: 'analyze-ecg' }"
        class="analyse flex items-center"
        exact-active-class="is-active"
      >
        <div class="icon-ecg"></div>
        <span>Analyze ECG</span>
      </nuxt-link>

      <nuxt-link
        v-for="(hospital, id) in HOSPITAL_CONFIG"
        :to="{ name: 'hospital-id', params: { id: hospital.id } }"
        class="hospital flex items-center"
        :key="id"
        exact-active-class="is-active"
      >
        <img
          :src="hospital.logoPath"
          alt="hospital-logo"
          width="40"
          height="40"
          class="hospital-logo"
        />
        <span>{{ hospital.name }}</span>
      </nuxt-link>
    </div>
  </div>
</template>

<script>
import { HOSPITAL_CONFIG } from '@/constants'

export default {
  name: 'Sidebar',
  data() {
    return {
      HOSPITAL_CONFIG,
    }
  },
}
</script>

<style lang="scss" scoped>
.sidebar {
  width: 300px;
  box-shadow: 0 0 1px rgba(0, 0, 0, 0.75);

  &__container {
    display: flex;
    flex-direction: column;

    position: sticky;
    top: 72px;

    .analyse {
      padding: 16px;

      .icon-ecg {
        background: url('../../static/ecg-icon.png') no-repeat;
        background-position: 50% 50%;
        background-size: 40px;

        width: 40px;
        height: 40px;
        margin-right: 5px;
      }

      &:hover {
        cursor: pointer;
        background-color: $primary-third;
      }

      &.is-active {
        background-color: $primary-secondary;
      }
    }

    .hospital {
      padding: 16px;
      height: 72px;

      .hospital-logo {
        margin-right: 5px;
      }

      .icon-hospital {
        background-position: 50% 50%;
        background-size: 40px;
      }

      &:hover {
        cursor: pointer;
        background-color: $primary-third;
      }

      &.is-active {
        background-color: $primary-secondary;
      }
    }
  }
}
</style>