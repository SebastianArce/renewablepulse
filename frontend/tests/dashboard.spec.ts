import { test, expect } from '@playwright/test'

const SNAPSHOT = {
  measured_at: '2026-06-30T20:00:00',
  generation: [
    { fuel_type: 'CCGT', generation_mw: 16228, share_pct: 57.35 },
    { fuel_type: 'WIND', generation_mw: 2060, share_pct: 7.28 },
  ],
  supply_demand: {
    settlement_period: 42,
    demand_mw: 27367,
    transmission_demand_mw: 31408,
    total_generation_mw: 28297,
  },
  carbon: {
    from_ts: '2026-06-30T19:00:00',
    intensity_gco2: 246,
    intensity_index: 'very high',
  },
}

const SUPPLY_DEMAND = [
  {
    period_start: '2026-06-30T19:30:00',
    settlement_period: 40,
    demand_mw: 27000,
    transmission_demand_mw: 31000,
    total_generation_mw: 27800,
  },
  {
    period_start: '2026-06-30T20:00:00',
    settlement_period: 41,
    demand_mw: 27367,
    transmission_demand_mw: 31408,
    total_generation_mw: 28297,
  },
]

test('dashboard renders live data from the API', async ({ page }) => {
  await page.route('**/api/snapshot', (route) => route.fulfill({ json: SNAPSHOT }))
  await page.route('**/api/supply-demand*', (route) =>
    route.fulfill({ json: SUPPLY_DEMAND }),
  )
  await page.route('**/api/events', (route) =>
    route.fulfill({ status: 200, contentType: 'text/event-stream', body: ': ok\n\n' }),
  )

  await page.goto('/')

  await expect(page.getByRole('heading', { name: 'TianguisWatt' })).toBeVisible()
  await expect(page.getByText('Generation mix')).toBeVisible()
  await expect(page.getByText('Supply vs demand')).toBeVisible()
  await expect(page.getByText('Carbon intensity')).toBeVisible()

  // data-derived text (rendered outside the ECharts canvas so it is assertable)
  await expect(page.getByText(/CCGT/)).toBeVisible()
  await expect(page.getByText(/very high/)).toBeVisible()
  await expect(page.getByText(/27367 MW/)).toBeVisible()
})
