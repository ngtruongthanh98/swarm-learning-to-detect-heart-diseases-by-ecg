export default function (req, res, next) {
  console.log(res.url)

  if(req.url === "/date") {
    res.end(JSON.stringify({date: new Date()}))
  }

  if(req.url === "/results") {
    res.end(JSON.stringify({hospitals: [
      {
        id: 0,
        name: "Swarm Learning",
        ecgResult: {
          id: 0,
          result: [
            {
              additionalClass: "bold",
              title: "Normal ECG",
              unit: "%",
              value: 70
            },
            {
              additionalClass: "bold",
              title: "Abnormal ECG",
              unit: "%",
              value: 5
            },
            {
              additionalClass: "bold",
              title: "Borderline ECG",
              unit: "%",
              value: 2
            },
            {
              additionalClass: "bold",
              title: "Borderline ECG",
              unit: "%",
              value: 23
            }
          ]
        }
      },
      {
        id: 1,
        name: "Cho Ray Hospital",
        ecgResult: {
          id: 1,
          result: [
            {
              additionalClass: "bold",
              title: "Normal ECG",
              unit: "%",
              value: 68
            },
            {
              additionalClass: "bold",
              title: "Abnormal ECG",
              unit: "%",
              value: 8
            },
            {
              additionalClass: "bold",
              title: "Borderline ECG",
              unit: "%",
              value: 3
            },
            {
              additionalClass: "bold",
              title: "Borderline ECG",
              unit: "%",
              value: 21
            }
          ]
        }
      },
      {
        id: 2,
        name: "Bach Mai Hospital",
        ecgResult: {
          id: 2,
          result: [
            {
              additionalClass: "bold",
              title: "Normal ECG",
              unit: "%",
              value: 72
            },
            {
              additionalClass: "bold",
              title: "Abnormal ECG",
              unit: "%",
              value: 4
            },
            {
              additionalClass: "bold",
              title: "Borderline ECG",
              unit: "%",
              value: 1
            },
            {
              additionalClass: "bold",
              title: "Borderline ECG",
              unit: "%",
              value: 23
            }
          ]
        }
      },
      {
        id: 3,
        name: "Tam Duc Hospital",
        ecgResult: {
          id: 3,
          result: [
            {
              additionalClass: "bold",
              title: "Normal ECG",
              unit: "%",
              value: 66
            },
            {
              additionalClass: "bold",
              title: "Abnormal ECG",
              unit: "%",
              value: 10
            },
            {
              additionalClass: "bold",
              title: "Borderline ECG",
              unit: "%",
              value: 4
            },
            {
              additionalClass: "bold",
              title: "Borderline ECG",
              unit: "%",
              value: 20
            }
          ]
        }
      },
      {
        id: 4,
        name: "Viet Phap Hospital",
        ecgResult: {
          id: 4,
          result: [
            {
              additionalClass: "bold",
              title: "Normal ECG",
              unit: "%",
              value: 80
            },
            {
              additionalClass: "bold",
              title: "Abnormal ECG",
              unit: "%",
              value: 5
            },
            {
              additionalClass: "bold",
              title: "Borderline ECG",
              unit: "%",
              value: 5
            },
            {
              additionalClass: "bold",
              title: "Borderline ECG",
              unit: "%",
              value: 10
            }
          ]
        }
      },
      {
        id: 5,
        name: "115 People's Hospital",
        ecgResult: {
          id: 5,
          result: [
            {
              additionalClass: "bold",
              title: "Normal ECG",
              unit: "%",
              value: 85
            },
            {
              additionalClass: "bold",
              title: "Abnormal ECG",
              unit: "%",
              value: 10
            },
            {
              additionalClass: "bold",
              title: "Borderline ECG",
              unit: "%",
              value: 5
            },
            {
              additionalClass: "bold",
              title: "Borderline ECG",
              unit: "%",
              value: 5
            }
          ]
        }
      },
    ]}))
  }


  if(req.url === "/result/0") {
    const resultList = [
      {
        title: 'Normal ECG',
        value: 80,
      },
      {
        title: 'Abnormal ECG',
        value: 5,
      },
      {
        title: 'Borderline ECG',
        value: 5,
      },
      {
        title: 'Otherwise normal ECG',
        value: 10,
      },
    ]

    res.end(JSON.stringify(resultList))
  }

  if(req.url === "/result/1") {
    const resultList = [
      {
        title: 'Normal ECG',
        value: 65,
      },
      {
        title: 'Abnormal ECG',
        value: 5,
      },
      {
        title: 'Borderline ECG',
        value: 20,
      },
      {
        title: 'Otherwise normal ECG',
        value: 10,
      },
    ]

    res.end(JSON.stringify(resultList))
  }

  if(req.url === "/result/2") {
    const resultList = [
      {
        title: 'Normal ECG',
        value: 50,
      },
      {
        title: 'Abnormal ECG',
        value: 10,
      },
      {
        title: 'Borderline ECG',
        value: 25,
      },
      {
        title: 'Otherwise normal ECG',
        value: 15,
      },
    ]

    res.end(JSON.stringify(resultList))
  }

  if(req.url === "/result/3") {
    const resultList = [
      {
        title: 'Normal ECG',
        value: 40,
      },
      {
        title: 'Abnormal ECG',
        value: 15,
      },
      {
        title: 'Borderline ECG',
        value: 30,
      },
      {
        title: 'Otherwise normal ECG',
        value: 15,
      },
    ]

    res.end(JSON.stringify(resultList))
  }

  if(req.url === "/result/4") {
    const resultList = [
      {
        title: 'Normal ECG',
        value: 35,
      },
      {
        title: 'Abnormal ECG',
        value: 20,
      },
      {
        title: 'Borderline ECG',
        value: 25,
      },
      {
        title: 'Otherwise normal ECG',
        value: 20,
      },
    ]

    res.end(JSON.stringify(resultList))
  }

  if(req.url === "/result/5") {
    const resultList = [
      {
        title: 'Normal ECG',
        value: 30,
      },
      {
        title: 'Abnormal ECG',
        value: 25,
      },
      {
        title: 'Borderline ECG',
        value: 20,
      },
      {
        title: 'Otherwise normal ECG',
        value: 25,
      },
    ]

    res.end(JSON.stringify(resultList))
  }



  next()
}
