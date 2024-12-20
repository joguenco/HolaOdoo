/** @odoo-module **/

import { registry } from '@web/core/registry'
import { useService } from '@web/core/utils/hooks'
import { OwlChartRenderer } from './chart/chart_renderer'

const { Component, useState, onWillStart } = owl

export class OwlGreetDashboard extends Component {
  setup() {
    this.state = useState({
      title: '',
      information: [],
      countModules: []
    })

    this.orm = useService('orm')

    onWillStart(async () => {
      console.log('onWillStart')
      this.state.title = 'Greetings Dashboard'
      console.log('this.state.title', this.state.title)

      this.state.information = await this.getModuleInformation()
      this.state.countModules = await this.countGroupModules()
    })
  }

  async getModuleInformation() {
    const information = await this.orm.searchRead(
      'ir.module.module',
      [['name', '=', 'greet']],
      ['author', 'description', 'shortdesc', 'website', 'summary']
    )

    console.log('information', information)

    return information
  }

  async countGroupModules() {
    const countModules = await this.orm.readGroup(
      'ir.module.module',
      [],
      ['state'],
      ['state']
    )

    console.log('countModules', countModules)

    return countModules
  } 
}

OwlGreetDashboard.template = 'owl.OwlGreetDashboard'
OwlGreetDashboard.components = { OwlChartRenderer }

registry.category('actions').add('owl.greet_dashboard', OwlGreetDashboard)
