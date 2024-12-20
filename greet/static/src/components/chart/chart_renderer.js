/** @odoo-module **/

import {
  loadJS
} from '@web/core/assets'

const {
  Component,
  useState,
  onWillStart,
  useRef,
  onMounted
} = owl

export class OwlChartRenderer extends Component {
  setup() {
    this.chartRef = useRef('chart')
    this.state = useState({
      title: this.props.title,
      type: this.props.type,
      data: this.props.data
    })

    onWillStart(async () => {
      await loadJS('https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.js')
    })

    onMounted(() => {
      console.log('Chart Renderer Mounted')

      console.log('Chart Renderer Data', this.state.data)

      const labels = []
      const metrics = []
      this.state.data.map((item) => {
        labels.push(item.state)
        metrics.push(item.state_count)
      })

      this.render(this.state.title, labels, metrics, this.state.type)
    })
  }

  render(title, labels, metrics, type = 'pie') {
    new Chart(this.chartRef.el, {
      type,
      data: {
        // labels: ['Red', 'Blue', 'Yellow'],
        labels: labels,
        datasets: [{
          label: title,
          // data: [12, 19, 3]
          data: metrics
        }]
      }
    })
  }
}

OwlChartRenderer.template = 'owl.OwlChartRenderer'
