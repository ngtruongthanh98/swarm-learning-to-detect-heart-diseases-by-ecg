<template>
  <client-only v-if="pieChartData" placeholder="Loading...">
    <PieChart
      :chartData="pieChartData"
      :options="[
        {
          hoverOffset: 4,
          rotation: 90,
          cutout: 10,
          hoverOffset: 30,
          hoverBorderWidth: 20,
        },
      ]"
      :height="90"
      :width="90"
    />
  </client-only>
</template>

<script>
export default {
  data() {
    return {
      pieChartData: {
        labels: [
          '2019-06',
          '2019-07',
          '2019-08',
          '2019-09',
          '2019-10',
          '2019-11',
        ],
        datasets: [
          {
            label: 'Visualization',
            data: [72, 131, 12, 3, 4, 55],
            backgroundColor: [
              '#99aa00',
              '#aabbee',
              '#990000',
              '#99ff00',
              '#994400',
              '#9900ff',
            ],
            borderColor: 'rgba(255, 255, 255, 1)',
            borderWidth: 2,
            radius: 240,
            hoverBackgroundColor: 'rgba(100, 0, 0, 0.5)',
            hoverOffset: 35,
          },
        ],
      },
    }
  },
}
</script>

<style>
</style>