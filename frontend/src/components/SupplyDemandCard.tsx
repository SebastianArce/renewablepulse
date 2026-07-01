import type { EChartsOption } from 'echarts'
import { useMemo } from 'react'
import { useSupplyDemandHistory } from '@/hooks/api'
import { useECharts } from '@/hooks/useECharts'
import { Card } from './Card'

export function SupplyDemandCard() {
  const { data } = useSupplyDemandHistory(12)

  const option = useMemo<EChartsOption>(() => {
    const points = data ?? []
    return {
      tooltip: { trigger: 'axis' },
      legend: { textStyle: { color: '#a3a3a3' }, top: 0 },
      grid: { left: 52, right: 16, top: 32, bottom: 28 },
      xAxis: { type: 'time', axisLabel: { color: '#737373' } },
      yAxis: { type: 'value', name: 'MW', axisLabel: { color: '#737373' } },
      series: [
        {
          name: 'Demand',
          type: 'line',
          showSymbol: false,
          data: points.map((p) => [p.period_start, p.demand_mw]),
        },
        {
          name: 'Generation',
          type: 'line',
          showSymbol: false,
          data: points.map((p) => [p.period_start, p.total_generation_mw]),
        },
      ],
    }
  }, [data])
  const chartRef = useECharts(option)
  const latest = data?.at(-1)

  return (
    <Card title="Supply vs demand" subtitle="National demand vs total generation">
      <div ref={chartRef} className="h-64 w-full" />
      {latest && (
        <p className="mt-2 text-sm text-neutral-300">
          Demand <span className="font-semibold">{latest.demand_mw} MW</span> ·
          Generation{' '}
          <span className="font-semibold">{latest.total_generation_mw} MW</span>
        </p>
      )}
    </Card>
  )
}
