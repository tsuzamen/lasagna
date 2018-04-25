import React from 'react';
import {
    BrowserRouter as Router,
    Route,
    Link
} from 'react-router-dom';

require('./App.css');

const Lasagna = ({ match }) => (
    <div>
      <p>Hi my name is Lasagna number {match.params.lasagnaId}</p>
    </div>
);

const Home = () => (
  <div>
    <h1>I think dogs should vote!</h1>
    <ul>
      <li><Link to='/lasagna/1'>1</Link></li>
      <li><Link to='/lasagna/2'>2</Link></li>
      <li><Link to='/lasagna/3'>3</Link></li>
    </ul>
  </div>
);

export default class App extends React.Component {
  constructor(props) {
    super(props);
    this.temp = true;
  }

  render() {
    return (
      <Router>
        <div>
          <Route exact path='/' component={Home}/>
          <Route path='/lasagna/:lasagnaId' component={Lasagna}/>
        </div>
      </Router>
    );
  }
}
