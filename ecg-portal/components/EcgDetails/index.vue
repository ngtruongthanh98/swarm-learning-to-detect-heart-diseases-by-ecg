<template>
  <div class="ecg-details-container">
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

        <div class="title">ECG Results Prediction</div>
      </div>

      <div class="result-ecg__boby">
        <div
          v-for="(ele, index) in RESULT_DATA_MOCK"
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
    </div>

    <div class="general-info">
      <div
        v-for="(ele, index) in GENERAL_DATA_MOCK"
        class="general-info__item"
        :key="index"
      >
        <div class="title">{{ ele.title }}</div>
        <div class="value">
          <span :class="ele.additionalClass">{{ ele.value }}</span>
          {{ ele.unit }}
        </div>
      </div>
    </div>

    <div class="heart-rate-and-ecg">
      <div class="heart-rate-and-ecg__header">
        <div class="header-icon">
          <div class="content">HR</div>
        </div>

        <div class="title">Heart Rate and ECG</div>
      </div>

      <div class="heart-rate-container">
        <div class="heart-rate-container__header">
          <div class="heart-rate-container__header-left">
            <div
              v-for="(ele, index) in HEART_RATE_DATA_MOCK"
              :key="index"
              class="item"
            >
              <div class="title">
                {{ ele.title }}
              </div>
              <div class="value">
                <span :class="ele.additionalClass">{{ ele.value }}</span>
                {{ ele.unit }}
              </div>
            </div>
          </div>
        </div>

        <ecg-viewer />
      </div>
    </div>
  </div>
</template>

<script>
import EcgViewer from '@/components/EcgViewer'

export default {
  components: {
    EcgViewer,
  },
  data() {
    return {
      GENERAL_DATA_MOCK: [
        {
          title: 'Risk',
          value: 'High',
          additionalClass: '',
          unit: '',
        },
        {
          title: 'Name',
          value: 'Hannibal',
          additionalClass: '',
          unit: '',
        },
        {
          title: 'Surname',
          value: 'Lecture',
          additionalClass: '',
          unit: '',
        },
        {
          title: 'Gender',
          value: 'M',
          additionalClass: '',
          unit: '',
        },
        {
          title: 'Age',
          value: '65',
          additionalClass: '',
          unit: '',
        },
        {
          title: 'Heart rate',
          value: '125',
          additionalClass: 'bold',
          unit: 'bpm',
        },
        {
          title: 'Repository rate',
          value: '28',
          additionalClass: 'bold',
          unit: 'bpm',
        },
        {
          title: 'Core temperature',
          value: '40.3',
          additionalClass: 'bold',
          unit: '°C',
        },
        {
          title: 'Oxygen saturation',
          value: '92',
          additionalClass: 'bold',
          unit: '%',
        },
      ],
      HEART_RATE_DATA_MOCK: [
        {
          title: 'Current',
          value: '65',
          additionalClass: 'bold',
          unit: 'bpm',
        },
        {
          title: 'Resting',
          value: '67',
          additionalClass: 'bold',
          unit: 'bpm',
        },
        {
          title: 'High',
          value: '180',
          additionalClass: 'bold',
          unit: 'bpm',
        },
      ],
      RESULT_DATA_MOCK: [
        {
          title: 'Normal ECG',
          value: '70%',
        },
        {
          title: 'Abnormal ECG',
          value: '5%',
        },
        {
          title: 'Borderline ECG',
          value: '2%',
        },
        {
          title: 'Otherwise normal ECG',
          value: '23%',
        },
      ],
    }
  },
}
</script>

<style lang="scss" scoped>
.ecg-details-container {
  display: flex;
  flex-direction: column;
  padding: 0 48px;

  .general-info {
    display: flex;
    justify-content: space-between;

    box-shadow: rgba(0, 0, 0, 0.08) 0px 4px 12px;
    border-radius: 5px;
    width: 100%;
    padding: 16px;
    margin-top: 32px;

    &:hover {
      box-shadow: rgba(14, 30, 37, 0.12) 0px 2px 4px 0px,
        rgba(14, 30, 37, 0.32) 0px 2px 16px 0px;
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
  }

  .result-ecg {
    display: flex;
    flex-direction: column;
    justify-content: space-between;

    padding: 16px;
    width: 50%;
    box-shadow: rgba(0, 0, 0, 0.08) 0px 4px 12px;
    border-radius: 5px;

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
  }

  .heart-rate-and-ecg {
    margin-top: 32px;
    width: 100%;

    box-shadow: rgba(0, 0, 0, 0.08) 0px 4px 12px;
    border-radius: 5px;

    &:hover {
      box-shadow: rgba(14, 30, 37, 0.12) 0px 2px 4px 0px,
        rgba(14, 30, 37, 0.32) 0px 2px 16px 0px;
    }

    &__header {
      display: flex;
      align-items: center;
      padding: 16px;

      .header-icon {
        background-color: orange;
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
      }
    }

    .heart-rate-container {
      padding: 0 16px;

      &__header {
        margin-bottom: 36px;

        &-left {
          display: flex;
          justify-content: space-between;
          max-width: 300px;

          .item {
            display: flex;
            flex-direction: column;

            .title {
              font-size: 14px;
            }

            .value {
              font-size: 20px;
            }
          }
        }
      }
    }
  }
}
</style>