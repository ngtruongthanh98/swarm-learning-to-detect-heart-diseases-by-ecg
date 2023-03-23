<template>
  <div class="result-ecg__container">
    <div class="result-ecg">
      <div class="result-ecg__header">
        <div class="header-icon">
          <div class="content">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              xmlns:xlink="http://www.w3.org/1999/xlink"
              width="16"
              height="16"
            >
              <defs>
                <linearGradient
                  id="b"
                  x1="-1483.396"
                  x2="-1155.767"
                  y1="1056.787"
                  y2="1056.787"
                  gradientUnits="userSpaceOnUse"
                  xlink:href="#a"
                />
                <linearGradient id="a">
                  <stop offset="0" stop-color="#fcd635" />
                  <stop offset="1" stop-color="#f7a928" />
                </linearGradient>
              </defs>
              <path
                fill="url(#b)"
                d="M-1220 1212.362c-11.656 8.326-86.446-44.452-100.77-44.568-14.324-.115-89.956 51.449-101.476 42.936-11.52-8.513 15.563-95.952 11.247-109.61-4.316-13.658-76.729-69.655-72.193-83.242 4.537-13.587 96.065-14.849 107.721-23.175 11.656-8.325 42.535-94.497 56.86-94.382 14.323.116 43.807 86.775 55.327 95.288 11.52 8.512 103.017 11.252 107.334 24.91 4.316 13.658-68.99 68.479-73.527 82.066-4.536 13.587 21.133 101.451 9.477 109.777z"
                color="#000"
                overflow="visible"
                transform="matrix(.04574 0 0 .04561 68.85 -40.34)"
                style="marker: none"
              />
            </svg>
          </div>
        </div>

        <div class="title">
          ECG Results Prediction
          <span class="sub-title">{{ '(' + extendedText + ')' }}</span>
        </div>
      </div>

      <div class="result-ecg__boby">
        <div
          v-for="(ele, index) in ecgResult"
          class="result-ecg__item"
          :key="index"
        >
          <div class="title">{{ ele.title }}</div>
          <div class="value">
            <span :class="ele.additionalClass">{{ ele.value }}</span>
            {{ ele.unit }}
          </div>
        </div>
      </div>

      <div class="button-container">
        <el-button type="primary" round @click="onClickViewDetails">{{
          isCollapsed ? 'View more' : 'View less'
        }}</el-button>
      </div>

      <div v-if="!isCollapsed" class="hospital-details">
        <div
          v-for="(ele, index) in HOSPITALS_DATA_MOCK"
          class="hospital-details__item"
          :key="index"
        >
          <div class="title">
            {{ ele.hospitalName }}
          </div>
          <div class="hospital">
            <div
              v-for="(item, id) in ele.resultList"
              class="hospital__item"
              :key="id"
            >
              <div class="attribute">
                {{ item.title }}
              </div>

              <div class="value">
                <span :class="item.additionalClass">{{ item.value }}</span>
                {{ item.unit }}
              </div>
            </div>
          </div>

          <div class="box-container">
            <div class="chart-box">
              <div class="chart-name">Predicted result</div>
              <pie-chart />
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="chart-container">
      <div class="chart-name">Overall result</div>
      <pie-chart />
    </div>
  </div>
</template>

<script>
import PieChart from '@/components/Chart/PieChart'
export default {
  components: {
    PieChart,
  },
  props: {
    extendedText: {
      type: String,
      required: true,
    },
    ecgResult: {
      type: Object,
      required: true,
    },
    hospitalId: {
      type: Number,
      required: true,
    },
  },
  data() {
    return {
      isCollapsed: true,
      RESULT_DATA_MOCK: [
        {
          title: 'Normal ECG',
          value: '70',
          additionalClass: 'bold',
          unit: '%',
        },
        {
          title: 'Abnormal ECG',
          value: '5',
          additionalClass: 'bold',
          unit: '%',
        },
        {
          title: 'Borderline ECG',
          value: '2',
          additionalClass: 'bold',
          unit: '%',
        },
        {
          title: 'Otherwise normal ECG',
          value: '23',
          additionalClass: 'bold',
          unit: '%',
        },
      ],
      HOSPITALS_DATA_MOCK: [
        {
          hospitalName: 'Cho Ray Hospital',
          resultList: [
            {
              title: 'Normal ECG',
              value: '70',
              additionalClass: 'bold',
              unit: '%',
            },
            {
              title: 'Abnormal ECG',
              value: '5',
              additionalClass: 'bold',
              unit: '%',
            },
            {
              title: 'Borderline ECG',
              value: '2',
              additionalClass: 'bold',
              unit: '%',
            },
            {
              title: 'Otherwise normal ECG',
              value: '23',
              additionalClass: 'bold',
              unit: '%',
            },
          ],
        },
        {
          hospitalName: 'Bach Mai Hospital',
          resultList: [
            {
              title: 'Normal ECG',
              value: '70',
              additionalClass: 'bold',
              unit: '%',
            },
            {
              title: 'Abnormal ECG',
              value: '5',
              additionalClass: 'bold',
              unit: '%',
            },
            {
              title: 'Borderline ECG',
              value: '2',
              additionalClass: 'bold',
              unit: '%',
            },
            {
              title: 'Otherwise normal ECG',
              value: '23',
              additionalClass: 'bold',
              unit: '%',
            },
          ],
        },
        {
          hospitalName: 'Tam Duc Hospital',
          resultList: [
            {
              title: 'Normal ECG',
              value: '70',
              additionalClass: 'bold',
              unit: '%',
            },
            {
              title: 'Abnormal ECG',
              value: '5',
              additionalClass: 'bold',
              unit: '%',
            },
            {
              title: 'Borderline ECG',
              value: '2',
              additionalClass: 'bold',
              unit: '%',
            },
            {
              title: 'Otherwise normal ECG',
              value: '23',
              additionalClass: 'bold',
              unit: '%',
            },
          ],
        },
        {
          hospitalName: 'Viet Phap Hospital',
          resultList: [
            {
              title: 'Normal ECG',
              value: '70',
              additionalClass: 'bold',
              unit: '%',
            },
            {
              title: 'Abnormal ECG',
              value: '5',
              additionalClass: 'bold',
              unit: '%',
            },
            {
              title: 'Borderline ECG',
              value: '2',
              additionalClass: 'bold',
              unit: '%',
            },
            {
              title: 'Otherwise normal ECG',
              value: '23',
              additionalClass: 'bold',
              unit: '%',
            },
          ],
        },
        {
          hospitalName: "115 People's Hospital",
          resultList: [
            {
              title: 'Normal ECG',
              value: '70',
              additionalClass: 'bold',
              unit: '%',
            },
            {
              title: 'Abnormal ECG',
              value: '5',
              additionalClass: 'bold',
              unit: '%',
            },
            {
              title: 'Borderline ECG',
              value: '2',
              additionalClass: 'bold',
              unit: '%',
            },
            {
              title: 'Otherwise normal ECG',
              value: '23',
              additionalClass: 'bold',
              unit: '%',
            },
          ],
        },
      ],
      chartData: {
        datasets: [
          {
            label: 'Title',
            data: [45, 55, 48, 35, 12],
          },
        ],
      },
      // pieChartData: {
      //   labels: [
      //     '2019-06',
      //     '2019-07',
      //     '2019-08',
      //     '2019-09',
      //     '2019-10',
      //     '2019-11',
      //   ],
      //   datasets: [
      //     {
      //       label: 'Visualization',
      //       data: [72, 131, 12, 3, 4, 55],
      //       backgroundColor: [
      //         '#99aa00',
      //         '#aabbee',
      //         '#990000',
      //         '#99ff00',
      //         '#994400',
      //         '#9900ff',
      //       ],
      //       borderColor: 'rgba(255, 255, 255, 1)',
      //       borderWidth: 2,
      //       radius: 240,
      //       hoverBackgroundColor: 'rgba(100, 0, 0, 0.5)',
      //       hoverOffset: 35,
      //     },
      //   ],
      // },
      // barChartOptions: {
      //   responsive: true,
      //   maintainAspectRatio: false,
      //   pointStyle: 'star',
      //   barThickness: 3,
      //   hoverOffset: 4,
      //   legend: {
      //     display: true,
      //     title: 'Pie Chart Samples',
      //   },
      //   title: {
      //     display: true,
      //     text: 'Customer analytics data',
      //     fontSize: 24,
      //     fontColor: '#6b7280',
      //   },
      //   tooltips: {
      //     backgroundColor: '#17BF62',
      //   },
      //   // scales: {
      //   //   xAxes: [
      //   //     {
      //   //       gridLines: {
      //   //         display: true
      //   //       }
      //   //     }
      //   //   ],
      //   //   yAxes: [
      //   //     {
      //   //       ticks: {
      //   //         beginAtZero: true,
      //   //         max: 7,
      //   //         min: 0,
      //   //         stepSize: 1
      //   //       },
      //   //       gridLines: {
      //   //         display: true
      //   //       }
      //   //     }
      //   //   ]
      //   // }
      // },
    }
  },
  methods: {
    onClickViewDetails() {
      this.isCollapsed = !this.isCollapsed
    },
  },
  mounted() {},
}
</script>

<style lang="scss" scoped>
.result-ecg__container {
  display: flex;

  .result-ecg {
    display: flex;
    flex-direction: column;
    justify-content: space-between;

    padding: 16px;
    width: 50%;
    height: fit-content;
    box-shadow: rgba(0, 0, 0, 0.08) 0px 4px 12px;
    border-radius: 5px;
    margin-right: 16px;

    &:hover {
      box-shadow: rgba(14, 30, 37, 0.12) 0px 2px 4px 0px,
        rgba(14, 30, 37, 0.32) 0px 2px 16px 0px;
    }

    &__header {
      display: flex;
      align-items: center;

      .header-icon {
        background-color: $error-color;
        width: 48px;
        height: 48px;
        border-radius: 5px;

        display: flex;
        align-items: center;
        justify-content: center;

        .content {
          color: white;
        }
      }

      .title {
        margin-left: 16px;
        font-size: 20px;
        font-weight: 500;

        .sub-title {
          font-size: 14px;
          font-style: italic;
        }
      }
    }

    &__boby {
      display: flex;
      justify-content: space-between;
      margin-top: 16px;
    }

    &__item {
      display: flex;
      flex-direction: column;

      .title {
        font-size: 14px;
      }

      .value {
        font-size: 20px;
        .bold {
          font-weight: 500;
        }
      }
    }

    .button-container {
      display: flex;
      justify-content: flex-end;
      margin-top: 16px;
    }

    .hospital-details {
      overflow: hidden;
      transition: height 200ms;

      &__item {
        margin-top: 24px;
        border-bottom: 1px solid black;
        display: flex;
        flex-direction: column;

        &:first-child {
          border-top: 1px solid black;
          padding-top: 16px;
        }
        &:last-child {
          border-bottom: none;
        }

        .title {
          font-weight: 500;
        }

        .hospital {
          display: flex;
          justify-content: space-between;
          padding-top: 8px;
          padding-bottom: 16px;

          &__item {
            display: flex;
            flex-direction: column;

            .attribute {
              font-size: 14px;
            }

            .value {
              font-size: 20px;
              .bold {
                font-weight: 500;
              }
            }
          }
        }
      }

      .box-container {
        width: 100%;
        display: flex;
        justify-content: center;

        .chart-box {
          width: 50%;
          border-radius: 5px;
          padding: 16px;
          height: fit-content;
          width: 300px;

          .chart-name {
            text-align: center;
          }
        }
      }
    }
  }

  .chart-container {
    box-shadow: rgba(0, 0, 0, 0.08) 0px 4px 12px;
    border-radius: 5px;
    padding: 16px;
    height: fit-content;
    margin-left: 16px;

    &:hover {
      box-shadow: rgba(14, 30, 37, 0.12) 0px 2px 4px 0px,
        rgba(14, 30, 37, 0.32) 0px 2px 16px 0px;
    }

    .chart-name {
      text-align: center;
    }
  }
}
</style>