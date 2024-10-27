import { Application } from '@tinyhttp/app'
import { serve } from '@cloudflare/workers-types'

const app = new Application()

app.all('*', async (req) => {
  const url = new URL(req.url)
  const response = await fetch(`http://127.0.0.1:8000${url.pathname}${url.search}`, {
    method: req.method,
    headers: req.headers,
    body: req.body
  })
  return response
})

export default {
  fetch: serve(app)
}

