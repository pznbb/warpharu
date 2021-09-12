# WarpPlusCloudflareHeroku

Automate Warp+ cloudflare with heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/HuzunluArtemis/WarpPlusCloudflareHeroku)

## Setting up config file
<details>
    <summary><b>Click Here For Details</b></summary><br>
  
- `WARP_ID`: Your warp+ id. Like: `asdf51saf15sa1d-as2d6f26a-31asd-aasd`
- `USE_PROXY`: I dont recommend use proxy mode. `True` or `False`. Default: `False`
- `PROXY_API`: Custom proxy api. Default: `https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all`
- `THREAD_COUNT`: Custom thread count for proxy mode. Dont give huge numbers. Your account may get banned. Default: `1000`
- `WAIT_SECS_FOR_NORMAL_MODE`: Waiting seconds between process. Default: `17`

</details>

## Thanks
<details>
    <summary><b>Click Here For Details</b></summary>
    <br>
Thanks to original developer: <a href="https://github.com/teppyboy/warp-plus-cloudflare">teppyboy &  ALIILAPRO</a> 
</details>


## License
<details>
    <summary><b>Click Here For Details</b></summary>
  <br>
  <a href="https://www.gnu.org/licenses/gpl-3.0.en.html">
  <img src="https://www.gnu.org/graphics/gplv3-127x51.png" alt="GNU GPLv3 Image">
</a>
<br><br>
WarpPlusCloudflareHeroku is Free Software: You can use, study share and improve it at your
will. Specifically you can redistribute and/or modify it under the terms of the 
  <a href="https://www.gnu.org/licenses/gpl.html">GNU General Public License</a> 
  as published by the Free Software Foundation, either version 3 of the License, 
  or (at your option) any later version.
</details>
