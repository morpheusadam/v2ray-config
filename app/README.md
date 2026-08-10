# notice.json — the message slot in v2rayV

`notice.json` is the only way to say something to a copy of v2rayV that is already
installed on someone's phone. The app reads it every six hours and draws whatever it finds
in the space below the Auto Mode card on the dashboard.

**Its normal state is the one it is in now: `"notice": null`, and the app shows nothing.**
Not an empty card — nothing. Leave it that way until there is something worth a person's
attention, because this slot appears inside a VPN app on someone's phone and spends
goodwill every time it is used.

The app reaches this file through the same route ladder Auto Mode uses — the raw host,
then CDN mirrors, then a public proxy — so it arrives on a network that blocks GitHub.

## Announcing an update

```json
{
  "version": 1,
  "notice": {
    "id": "update-2.4.0",
    "title": "Update available",
    "body": "2.4.0 finds a working proxy when GitHub is blocked, and connects on the first server fast enough for your line.",
    "accent": "green",
    "maxVersionCode": 743,
    "dismissible": true,
    "action": {
      "label": "Update",
      "type": "install",
      "url": "https://github.com/morpheusadam/v2rayV/releases/download/v2.4.0/v2rayV-arm64-v8a.apk"
    }
  }
}
```

**`maxVersionCode` is the field to get right.** It is the last version that should still see
the notice — the one *before* the release being announced. Leave it out and the card
follows people onto the version it told them to install and never goes away.

`versionCode` for a given release is in `V2rayNG/app/build.gradle.kts`.

## Fields

| Field | Meaning |
|---|---|
| `id` | Stable identifier. Dismissal is remembered against it, so editing the text without changing the id will not bring it back for anyone who dismissed it — and changing the id will. |
| `title` | The coloured line. Rendered in small caps. |
| `body` | Up to four lines, then it is ellipsised. |
| `accent` | `green`, `violet` or `red`. Anything else reads as green. |
| `minVersionCode` | Only versions at or above this see it. `0` means no lower bound. |
| `maxVersionCode` | Only versions at or below this see it. `0` means no upper bound. |
| `dismissible` | `false` removes the dismiss button. Use sparingly — it means the card cannot be got rid of. |
| `action` | The single button, or omit it for a card that only says something. |

### `action.type`

- `install` — downloads the APK and raises Android's install dialog. **The URL must be
  HTTPS on `github.com`**; the app refuses anything else, and Android refuses an APK that
  is not signed with the same key as the installed app.
- `url` — opens the link in a browser.

## What it cannot do

The slot renders a title, a body and at most one button. There is no markup, no image, no
scripting, and no action other than opening a URL or offering an APK. That is deliberate:
a file in a git repository that can decide what an installed VPN app does is worth keeping
narrow, and a wider channel would be one more thing to get right forever.

## Turning it off again

Set `"notice": null`. Anyone who has not opened the app since the last fetch will simply
never see it; anyone who has will lose it within six hours.
