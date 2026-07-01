import type { EChartsOption } from 'echarts'
import { useMemo } from 'react'
import { useSnapshot } from '@/hooks/api'
import { useECharts } from '@/hooks/useECharts'
import { Card } from './Card'

export function CarbonCard() {
  const { data } = useSnapshot()
  const carbon = data?.carbon
  const value = carbon?.intensity_gco2 ?? 0

  const option = useMemo<EChartsOption>(
    () => ({
      series: [
        {
          type: 'gauge',
          min: 0,
          max: 500,
          progress: { show: true, width: 12 },
          axisLine: { lineStyle: { width: 12 } },
          axisLabel: { color: '#737373', distance: 14, fontSize: 10 },
          detail: { formatter: '{value}', color: '#e5e5e5', fontSize: 24 },
          data: [{ value }],
        },
      ],
    }),
    [value],
  )
  const chartRef = useECharts(option)

  return (
    <Card title="Carbon intensity" subtitle="Grams of CO₂ per kWh, national">
      <div ref={chartRef} className="h-64 w-full" />
      {carbon && (
        <p className="mt-2 text-sm text-neutral-300">
          <span className="font-semibold">{carbon.intensity_gco2}</span> gCO₂/kWh ·{' '}
          {carbon.intensity_index}
        </p>
      )}
    </Card>
  )
}
