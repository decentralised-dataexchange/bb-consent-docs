# Webhooks

Manage webhooks for user events. Webhooks allow external services to be notified when certain events happen.

In webhooks page, the organisation admin can perform following:

1. View list of webhooks endpoints configured
2. CRUD webhook endpoints. Each webhook endpoint has a status, which indicates whether the webhook endpoint currently down or up.
3. On create/update, organisation admin has to specify the following details:
   1. Payload URL - Webhook URL to which the payload is send to.
   2. Content type - Content type to be used for webhook payload
   3. Skip SSL verification - To skip ssl certificate verificate when sending the webhook using http client
   4. Secret key - Webhook URL can check if the recieved event is indeed from a trusted source.
   5. Events to subscribe, i.e when these events occur, it will trigger the webhook
      1. When individuals opt-in to a data agreement (consent.allowed)
      2. When individuals opt-out of a data agreement (consent.disallowed)
4. On clicking the webhook, it is possible to see list of recent deliveries made to it, whether it was successfully delivered or not, time of delivery and delivery id.