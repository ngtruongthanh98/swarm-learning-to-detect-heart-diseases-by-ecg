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

        <div class="title">
          ECG Results Prediction
          <span class="sub-title">{{ '(' + extendedText + ')' }}</span>
        </div>
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
      <div class="general-info__header">
        <div class="header-icon">
          <div class="content">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32">
              <title>medical document</title>
              <g id="document" fill="#fff">
                <path
                  d="M27.59,22.19,26,21V5.3A3.3,3.3,0,0,0,22.7,2H10.3A3.3,3.3,0,0,0,7,5.3V11H5a1,1,0,0,0-1,1V27.07A2.94,2.94,0,0,0,6.93,30H25.07A2.94,2.94,0,0,0,28,27.07V23A1,1,0,0,0,27.59,22.19ZM9,5.3A1.3,1.3,0,0,1,10.3,4H22.7A1.3,1.3,0,0,1,24,5.3V19.56L12.59,11.19A1,1,0,0,0,12,11H9ZM26,27.07a.93.93,0,0,1-.93.93H6.93A.93.93,0,0,1,6,27.07V13h5.67L26,23.51ZM12,8a1,1,0,0,1,1-1h7a1,1,0,0,1,0,2H13A1,1,0,0,1,12,8Zm9,3a1,1,0,0,1-1,1H17a1,1,0,0,1,0-2h3A1,1,0,0,1,21,11Z"
                />
              </g>
            </svg>
          </div>
        </div>

        <div class="title">General Info</div>
      </div>

      <div class="general-info__body">
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
  props: {
    extendedText: {
      type: String,
      default: '',
    },
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

  .result-ecg,
  .general-info {
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
  }

  .general-info {
    margin-top: 32px;
    width: 100%;

    &__header {
      .header-icon {
        background-color: $light-blue;

        svg {
          width: 32px;
          height: 32px;
        }
      }
    }

    &__body {
      display: flex;
      justify-content: space-between;
      padding-top: 16px;
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