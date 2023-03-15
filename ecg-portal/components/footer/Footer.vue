<template>
  <footer class="footer-wrapper">
    <p>Copyright &copy; {{ year }}</p>
    <a
      href="https://github.com/ngtruongthanh98/swarm-learning-to-detect-heart-diseases-by-ecg"
      target="_blank"
      rel="noopener"
      class="hover:text-gray-800"
    >
      <svg
        xmlns="http://www.w3.org/2000/svg"
        class="h-6 w-6 inline-block mr-2"
        viewBox="0 0 20 20"
        fill="currentColor"
      >
        <path
          fill-rule="evenodd"
          d="M10 0a10 10 0 0 0-3.16 19.49c.5.09.68-.22.68-.49l-.01-1.71c-2.78.6-3.37-1.34-3.37-1.34-.45-1.14-1.11-1.44-1.11-1.44-.91-.63.07-.62.07-.62 1 .07 1.53 1.03 1.53 1.03.89 1.52 2.34 1.08 2.91.83.09-.65.35-1.08.64-1.33-2.24-.25-4.59-1.12-4.59-4.98 0-1.1.39-2 1.03-2.7-.1-.25-.45-1.28.1-2.67 0 0 .85-.27 2.78 1.03a9.8 9.8 0 0 1 2.53-.34c.86 0 1.73.12 2.53.34 1.93-1.3 2.78-1.03 2.78-1.03.55 1.39.2 2.42.1 2.67.64.7 1.03 1.6 1.03 2.7 0 3.87-2.35 4.72-4.59 4.97.36.31.68.92.68 1.85l-.01 2.75c0 .27.18.58.69.48A10 10 0 0 0 10 0z"
          clip-rule="evenodd"
        />
      </svg>
      GitHub
    </a>
  </footer>
</template>

<script>
export default {
  name: 'VmFooter',
  data() {
    return {
      year: new Date().getFullYear(),
    }
  },
}
</script>

<style lang="scss" scoped>
.link {
  @apply hover:underline;
  @apply hover:opacity-75;
}
.footer-wrapper {
  background-color: $primary-secondary;
  height: 80px;

  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 32px;

  color: $white-color;
}
</style>
