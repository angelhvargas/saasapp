import React, {Component} from 'react'
import PropTypes from 'prop-types'


export default class App extends React.Component {

  static propTypes = {
    children: PropTypes.element.isRequired
  }

  render() {

    return (
      <main>
        {this.props.children}
      </main>
    )
  }
}
