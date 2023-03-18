<template>
  <div class="ecg-details-container">
    <div class="result-ecg">
      <div
        v-for="(ele, index) in RESULT_DATA_MOCK"
        class="result-ecg__item"
        :key="index"
      >
        <div class="title">{{ ele.title }}</div>
        <div class="value">{{ ele.value }}</div>
      </div>
    </div>

    <div class="general-info">
      <div
        v-for="(ele, index) in GENERAL_DATA_MOCK"
        class="general-info__item"
        :key="index"
      >
        <div class="title">{{ ele.title }}</div>
        <div class="value">{{ ele.value }}</div>
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
                {{ ele.value }}
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
        },
        {
          title: 'Name',
          value: 'Hannibal',
        },
        {
          title: 'Surname',
          value: 'Lecture',
        },
        {
          title: 'Gender',
          value: 'M',
        },
        {
          title: 'Age',
          value: '65',
        },
        {
          title: 'Heart rate',
          value: '125 bpm',
        },
        {
          title: 'Repository rate',
          value: '28 bpm',
        },
        {
          title: 'Core temperature',
          value: '40.3 °C',
        },
        {
          title: 'Oxygen saturation',
          value: '92%',
        },
      ],
      HEART_RATE_DATA_MOCK: [
        {
          title: 'Current',
          value: '65 bpm',
        },
        {
          title: 'Resting',
          value: '67 bpm',
        },
        {
          title: 'High',
          value: '180 bpm',
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

    border: 1px solid black;
    border-radius: 5px;
    width: 100%;
    padding: 16px;
    margin-top: 32px;

    &__item {
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

  .result-ecg {
    display: flex;
    justify-content: space-between;

    padding: 16px;
    width: 50%;
    border: 1px solid black;
    border-radius: 5px;

    &__item {
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

  .heart-rate-and-ecg {
    margin-top: 32px;
    width: 100%;

    border: 1px solid black;
    border-radius: 5px;

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