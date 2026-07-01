import { test, expect } from '@playwright/test'

test('home page renders the app title', async ({ page }) => {
  await page.goto('/')
  await expect(
    page.getByRole('heading', { name: 'RenewablePulse' }),
  ).toBeVisible()
})
