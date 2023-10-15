import React from 'react';
import { Chart } from 'react-google-charts';

const ShowerChart = ({ data }) => {
  return (
    <Chart
      width={'800px'}
      height={'400px'}
      chartType="LineChart"
      loader={<div>Loading Chart</div>}
      data={[
        ['Date', 'Duration (minutes)'],
        ...Object.keys(data).map(key => [
          data[key].date,
          parseInt(data[key].duration_minutes)
        ])
      ]}
      options={{
        title: 'Shower Duration From August 15th',
        titleTextStyle: {
          color: '#ffffff' 
        },
        hAxis: {
          title: '',
          textStyle: {
            color: '#ffffff' 
          },
          titleTextStyle: {
            color: '#ffffff'
          }
        },
        vAxis: {
          title: 'Duration (minutes)',
          textStyle: {
            color: '#ffffff'
          },
          titleTextStyle: {
            color: '#ffffff'
          }
        },
        legend: {
          textStyle: {
            color: '#ffffff'
          }
        },
        backgroundColor: '#242424', 
        colors: ['#00FF00'], 
      }}
      rootProps={{ 'data-testid': '1' }}
    />
  );
};

export default ShowerChart;