<template>
  <div class="about-page">
    <card
      :title="ecgTitle"
      :card-content="ecgDefinition"
      className="ecg-definition-card"
    />

    <el-card class="image-card">
      <img src="@/static/electrocardiogram.jpg" alt="ECG image" width="400px" />
    </el-card>
  </div>
</template>

<script>
import Card from '@/components/Card/Card'
export default {
  data() {
    return {
      ecgTitle: 'What is ECG?',
      ecgDefinition:
        "Electrocardiography (ECG aka EKG) is the process of producing an electrocardiogram, a recording of the heart's electrical activity through repeated cardiac cycles. It is an electrogram of the heart which is a graph of voltage versus time of the electrical activity of the heart using electrodes placed on the skin.",
    }
  },
  components: {
    Card,
  },
}
</script>

<style lang="scss" scoped>
.about-page {
  min-height: calc(100vh - 80px - 80px);

  display: flex;
  flex-direction: column;
  align-items: center;

  .ecg-definition-card {
    margin-top: 48px;
    margin-bottom: 16px;

    &:hover {
      background-color: $primary-third;
    }
  }

  .image-card {
    width: 480px;
    margin-top: 16px;
    margin-bottom: 16px;
  }
}
</style>