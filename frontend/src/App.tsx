import { CarbonCard } from '@/components/CarbonCard'
import { GenerationMixCard } from '@/components/GenerationMixCard'
import { SupplyDemandCard } from '@/components/SupplyDemandCard'
import { useLiveUpdates } from '@/hooks/useLiveUpdates'

export default function App() {
  useLiveUpdates()

  return (
    <main className="min-h-screen bg-neutral-950 text-neutral-100">
      <header className="border-b border-neutral-800 px-6 py-5">
        <h1 className="text-2xl font-bold tracking-tight">RenewablePulse</h1>
        <p className="text-sm text-neutral-400">
          A live view of the GB electricity market — the charts update automatically as
          new data arrives.
        </p>
      </header>
      <div className="grid gap-4 p-6 md:grid-cols-2 xl:grid-cols-3">
        <GenerationMixCard />
        <SupplyDemandCard />
        <CarbonCard />
      </div>
    </main>
  )
}
