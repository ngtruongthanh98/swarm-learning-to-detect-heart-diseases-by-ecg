<template>
  <client-only v-if="pieChartData" placeholder="Loading...">
    <PieChart
      :chartData="pieChartData"
      :chart-id="chartId"
      :dataset-id-key="datasetIdKey"
      :plugins="plugins"
      :css-classes="cssClasses"
      :styles="styles"
      :width="width"
      :height="height"
    />
  </client-only>
</template>

<script>
export default {
  props: {
    chartId: {
      type: String,
      default: 'pie-chart',
    },
    datasetIdKey: {
      type: String,
      default: 'label',
    },
    width: {
      type: Number,
      default: 300,
    },
    height: {
      type: Number,
      default: 300,
    },
    cssClasses: {
      default: '',
      type: String,
    },
    styles: {
      type: Object,
      default: () => {},
    },
    plugins: {
      type: Array,
      default: () => [],
    },
  },
  data() {
    return {
      pieChartData: {
        labels: [
          'Normal ECG',
          'Abnormal ECG',
          'Borderline ECG',
          'Otherwise normal ECG',
        ],
        datasets: [
          {
            label: 'Visualization',
            data: [70, 5, 2, 23],
            backgroundColor: ['#017DD3', '#ED7D28', '#D23A1D', '#F5E18F'],
            borderColor: 'rgba(255, 255, 255, 1)',
          },
        ],
      },
    }
  },
}
</script>

<style>
</style>