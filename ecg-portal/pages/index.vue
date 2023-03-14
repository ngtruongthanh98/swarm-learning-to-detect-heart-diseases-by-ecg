<template>
  <div>
    <VmHero />
    <VmSubheader />
  </div>
</template>

<script>
import VmHero from '@/components/hero/Hero'
import VmSubheader from '@/components/subheader/Subheader'

export default {
  name: 'index',
  components: {
    VmHero,
    VmSubheader,
  },
}
</script>
