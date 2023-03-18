<template>
  <nav
    class="flex justify-between sticky top-0 bg-white z-10 custom-navbar"
    role="navigation"
    aria-label="main navigation"
  >
    <nuxt-link
      :to="{ name: 'index' }"
      class="app-logo navbar-item flex items-center"
    >
      <h1 class="title w-16 h-12"></h1>
      <span class="logo-title">ECG Portal</span>
    </nuxt-link>

    <div class="flex items-center hospital-container">
      <nuxt-link
        :to="{ name: 'analyze-ecg' }"
        class="analyse flex items-center"
        exact-active-class="is-active"
      >
        <div class="icon-ecg"></div>
        <span>Analyze ECG</span>
      </nuxt-link>

      <nuxt-link
        :to="{ name: 'about-ecg' }"
        class="about flex items-center"
        exact-active-class="is-active"
      >
        <div class="icon-ecg w-20 h-12"></div>
        <span>About ECG</span>
      </nuxt-link>
    </div>
  </nav>
</template>


<script>
export default {
  name: 'VmHeader',
}
</script>

<style lang="scss" scoped>
.custom-navbar {
  box-shadow: rgba(0, 0, 0, 0.05) 0px 0px 0px 1px,
    rgb(209, 213, 219) 0px 0px 0px 1px inset;
}

.app-logo {
  padding: 16px;

  .logo-title {
    font-weight: 500;
    margin-left: 4px;
  }
}

.title {
  background: url('../../static/heart-logo.png') no-repeat;
  background-position: 50% 50%;
  background-size: 40px;
}

.hospital-container {
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
      box-shadow: rgba(0, 0, 0, 0.35) 0px 5px 15px;
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
      background-color: $primary-third;
    }

    &.is-active {
      background-color: $primary-secondary;
      box-shadow: rgba(0, 0, 0, 0.35) 0px 5px 15px;
    }
  }
}
</style>
