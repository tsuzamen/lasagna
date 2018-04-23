import React from 'react';

require('./App.css');

export default class App extends React.Component {
  constructor(props) {
    super(props);
    this.temp = true;
  }

  render() {
    return (
      <h1>I think dogs should vote!</h1>
    );
  }
}
