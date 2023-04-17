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
    hospitalId: {
      type: Number,
      required: true,
    },
  },
  data() {
    return {
      pieChartData: {
        lables: [],
        datasets: [
          {
            label: 'Visualization',
            data: [],
            backgroundColor: ['#017DD3', '#ED7D28', '#D23A1D', '#F5E18F'],
            borderColor: 'rgba(255, 255, 255, 1)',
          },
        ],
      },
      hospitalData: {},
      ecgTypes: [],
      ecgValues: [],
    }
  },
  mounted() {
    this.hospitalData = this.$store.getters.getHospitalById(this.hospitalId)

    const ecgTypes = this.hospitalData.ecgResult.result.map(ecg => ecg.title);
    const ecgValues = this.hospitalData.ecgResult.result.map(ecg => ecg.value);


    this.pieChartData = {
      labels: ecgTypes,
      datasets: [
        {
          label: 'Visualization',
          data: ecgValues,
          backgroundColor: ['#017DD3', '#ED7D28', '#D23A1D', '#F5E18F'],
          borderColor: 'rgba(255, 255, 255, 1)',
        },
      ],
    };
  }

}
</script>

<style>
</style>