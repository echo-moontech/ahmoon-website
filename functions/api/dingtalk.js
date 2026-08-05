export async function onRequestPost(context) {
  try {
    const body = await context.request.json();

    const accessToken = 'f38a7b24fbd66713478a856d566aa7af7c232405c47910bc673163c1820a781b';
    const secret = 'SECb4b595d3a22512653306edfedf21ffbe59cfd6413883bb31c6661f27be635e58';

    const timestamp = Date.now();
    const stringToSign = timestamp + '\n' + secret;
    const encoder = new TextEncoder();
    const keyData = encoder.encode(secret);
    const msgData = encoder.encode(stringToSign);

    const cryptoKey = await crypto.subtle.importKey(
      'raw', keyData, { name: 'HMAC', hash: 'SHA-256' }, false, ['sign']
    );
    const signature = await crypto.subtle.sign('HMAC', cryptoKey, msgData);
    const sign = btoa(String.fromCharCode(...new Uint8Array(signature)));

    const dingtalkUrl = 'https://oapi.dingtalk.com/robot/send?access_token=' + accessToken +
      '&timestamp=' + timestamp + '&sign=' + encodeURIComponent(sign);

    const response = await fetch(dingtalkUrl, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(body)
    });

    const data = await response.json();
    return new Response(JSON.stringify(data), {
      headers: {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      }
    });
  } catch (err) {
    return new Response(JSON.stringify({ errcode: -1, errmsg: err.message }), {
      status: 500,
      headers: {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      }
    });
  }
}

export async function onRequestOptions() {
  return new Response(null, {
    headers: {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'POST, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type'
    }
  });
}