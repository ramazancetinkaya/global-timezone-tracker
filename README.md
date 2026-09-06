# Global Country Timezone and UTC/GMT Dataset

An automated reference tracking real-time UTC/GMT offsets, Daylight Saving Time (DST) transitions, and ISO 3166-1 country mappings. Updated weekly via GitHub Actions.

## Dataset Metadata

| Metric | Specification |
| :--- | :--- |
| Last Synchronization | 2026-09-06 03:30:28 UTC |
| Countries Tracked | 247 |
| Timezones Tracked | 418 |
| Update Cadence | Weekly (Every Sunday at 00:00 UTC) |
| Raw Data Export | [timezones.json](./timezones.json) |
| Pipeline Telemetry | [last_run.json](./last_run.json) |

## Data Schema

The compiled `timezones.json` provides a clean and uniform structure suitable for direct consumption in backend or frontend applications:

```json
[
  {
    "country_code": "TR",
    "country_name": "Turkey",
    "zones": [
      {
        "timezone": "Europe/Istanbul",
        "gmt_offset": "UTC+03:00",
        "offset_seconds": 10800,
        "is_dst": false
      }
    ]
  }
]
```

## Active Reference Table

| Country | ISO Code | Timezone Identifier | UTC Offset | DST Active |
| :--- | :---: | :--- | :---: | :---: |
| Afghanistan | `AF` | `Asia/Kabul` | `UTC+04:30` | No |
| Albania | `AL` | `Europe/Tirane` | `UTC+02:00` | Yes |
| Algeria | `DZ` | `Africa/Algiers` | `UTC+01:00` | No |
| Andorra | `AD` | `Europe/Andorra` | `UTC+02:00` | Yes |
| Angola | `AO` | `Africa/Luanda` | `UTC+01:00` | No |
| Anguilla | `AI` | `America/Anguilla` | `UTC-04:00` | No |
| Antarctica | `AQ` | `Antarctica/McMurdo` | `UTC+12:00` | No |
|  |  | `Antarctica/Casey` | `UTC+08:00` | No |
|  |  | `Antarctica/Davis` | `UTC+07:00` | No |
|  |  | `Antarctica/DumontDUrville` | `UTC+10:00` | No |
|  |  | `Antarctica/Mawson` | `UTC+05:00` | No |
|  |  | `Antarctica/Palmer` | `UTC-03:00` | No |
|  |  | `Antarctica/Rothera` | `UTC-03:00` | No |
|  |  | `Antarctica/Syowa` | `UTC+03:00` | No |
|  |  | `Antarctica/Troll` | `UTC+02:00` | Yes |
|  |  | `Antarctica/Vostok` | `UTC+05:00` | No |
| Antigua & Barbuda | `AG` | `America/Antigua` | `UTC-04:00` | No |
| Argentina | `AR` | `America/Argentina/Buenos_Aires` | `UTC-03:00` | No |
|  |  | `America/Argentina/Cordoba` | `UTC-03:00` | No |
|  |  | `America/Argentina/Salta` | `UTC-03:00` | No |
|  |  | `America/Argentina/Jujuy` | `UTC-03:00` | No |
|  |  | `America/Argentina/Tucuman` | `UTC-03:00` | No |
|  |  | `America/Argentina/Catamarca` | `UTC-03:00` | No |
|  |  | `America/Argentina/La_Rioja` | `UTC-03:00` | No |
|  |  | `America/Argentina/San_Juan` | `UTC-03:00` | No |
|  |  | `America/Argentina/Mendoza` | `UTC-03:00` | No |
|  |  | `America/Argentina/San_Luis` | `UTC-03:00` | No |
|  |  | `America/Argentina/Rio_Gallegos` | `UTC-03:00` | No |
|  |  | `America/Argentina/Ushuaia` | `UTC-03:00` | No |
| Armenia | `AM` | `Asia/Yerevan` | `UTC+04:00` | No |
| Aruba | `AW` | `America/Aruba` | `UTC-04:00` | No |
| Australia | `AU` | `Australia/Lord_Howe` | `UTC+10:30` | No |
|  |  | `Antarctica/Macquarie` | `UTC+10:00` | No |
|  |  | `Australia/Hobart` | `UTC+10:00` | No |
|  |  | `Australia/Melbourne` | `UTC+10:00` | No |
|  |  | `Australia/Sydney` | `UTC+10:00` | No |
|  |  | `Australia/Broken_Hill` | `UTC+09:30` | No |
|  |  | `Australia/Brisbane` | `UTC+10:00` | No |
|  |  | `Australia/Lindeman` | `UTC+10:00` | No |
|  |  | `Australia/Adelaide` | `UTC+09:30` | No |
|  |  | `Australia/Darwin` | `UTC+09:30` | No |
|  |  | `Australia/Perth` | `UTC+08:00` | No |
|  |  | `Australia/Eucla` | `UTC+08:45` | No |
| Austria | `AT` | `Europe/Vienna` | `UTC+02:00` | Yes |
| Azerbaijan | `AZ` | `Asia/Baku` | `UTC+04:00` | No |
| Bahamas | `BS` | `America/Nassau` | `UTC-04:00` | Yes |
| Bahrain | `BH` | `Asia/Bahrain` | `UTC+03:00` | No |
| Bangladesh | `BD` | `Asia/Dhaka` | `UTC+06:00` | No |
| Barbados | `BB` | `America/Barbados` | `UTC-04:00` | No |
| Belarus | `BY` | `Europe/Minsk` | `UTC+03:00` | No |
| Belgium | `BE` | `Europe/Brussels` | `UTC+02:00` | Yes |
| Belize | `BZ` | `America/Belize` | `UTC-06:00` | No |
| Benin | `BJ` | `Africa/Porto-Novo` | `UTC+01:00` | No |
| Bermuda | `BM` | `Atlantic/Bermuda` | `UTC-03:00` | Yes |
| Bhutan | `BT` | `Asia/Thimphu` | `UTC+06:00` | No |
| Bolivia | `BO` | `America/La_Paz` | `UTC-04:00` | No |
| Bosnia & Herzegovina | `BA` | `Europe/Sarajevo` | `UTC+02:00` | Yes |
| Botswana | `BW` | `Africa/Gaborone` | `UTC+02:00` | No |
| Brazil | `BR` | `America/Noronha` | `UTC-02:00` | No |
|  |  | `America/Belem` | `UTC-03:00` | No |
|  |  | `America/Fortaleza` | `UTC-03:00` | No |
|  |  | `America/Recife` | `UTC-03:00` | No |
|  |  | `America/Araguaina` | `UTC-03:00` | No |
|  |  | `America/Maceio` | `UTC-03:00` | No |
|  |  | `America/Bahia` | `UTC-03:00` | No |
|  |  | `America/Sao_Paulo` | `UTC-03:00` | No |
|  |  | `America/Campo_Grande` | `UTC-04:00` | No |
|  |  | `America/Cuiaba` | `UTC-04:00` | No |
|  |  | `America/Santarem` | `UTC-03:00` | No |
|  |  | `America/Porto_Velho` | `UTC-04:00` | No |
|  |  | `America/Boa_Vista` | `UTC-04:00` | No |
|  |  | `America/Manaus` | `UTC-04:00` | No |
|  |  | `America/Eirunepe` | `UTC-05:00` | No |
|  |  | `America/Rio_Branco` | `UTC-05:00` | No |
| Britain (UK) | `GB` | `Europe/London` | `UTC+01:00` | Yes |
| British Indian Ocean Territory | `IO` | `Indian/Chagos` | `UTC+06:00` | No |
| Brunei | `BN` | `Asia/Brunei` | `UTC+08:00` | No |
| Bulgaria | `BG` | `Europe/Sofia` | `UTC+03:00` | Yes |
| Burkina Faso | `BF` | `Africa/Ouagadougou` | `UTC+00:00` | No |
| Burundi | `BI` | `Africa/Bujumbura` | `UTC+02:00` | No |
| Cambodia | `KH` | `Asia/Phnom_Penh` | `UTC+07:00` | No |
| Cameroon | `CM` | `Africa/Douala` | `UTC+01:00` | No |
| Canada | `CA` | `America/St_Johns` | `UTC-02:30` | Yes |
|  |  | `America/Halifax` | `UTC-03:00` | Yes |
|  |  | `America/Glace_Bay` | `UTC-03:00` | Yes |
|  |  | `America/Moncton` | `UTC-03:00` | Yes |
|  |  | `America/Goose_Bay` | `UTC-03:00` | Yes |
|  |  | `America/Blanc-Sablon` | `UTC-04:00` | No |
|  |  | `America/Toronto` | `UTC-04:00` | Yes |
|  |  | `America/Iqaluit` | `UTC-04:00` | Yes |
|  |  | `America/Atikokan` | `UTC-05:00` | No |
|  |  | `America/Winnipeg` | `UTC-05:00` | Yes |
|  |  | `America/Resolute` | `UTC-05:00` | Yes |
|  |  | `America/Rankin_Inlet` | `UTC-05:00` | Yes |
|  |  | `America/Regina` | `UTC-06:00` | No |
|  |  | `America/Swift_Current` | `UTC-06:00` | No |
|  |  | `America/Edmonton` | `UTC-06:00` | Yes |
|  |  | `America/Cambridge_Bay` | `UTC-06:00` | Yes |
|  |  | `America/Inuvik` | `UTC-06:00` | Yes |
|  |  | `America/Vancouver` | `UTC-07:00` | Yes |
|  |  | `America/Creston` | `UTC-07:00` | No |
|  |  | `America/Dawson_Creek` | `UTC-07:00` | No |
|  |  | `America/Fort_Nelson` | `UTC-07:00` | No |
|  |  | `America/Whitehorse` | `UTC-07:00` | No |
|  |  | `America/Dawson` | `UTC-07:00` | No |
| Cape Verde | `CV` | `Atlantic/Cape_Verde` | `UTC-01:00` | No |
| Caribbean NL | `BQ` | `America/Kralendijk` | `UTC-04:00` | No |
| Cayman Islands | `KY` | `America/Cayman` | `UTC-05:00` | No |
| Central African Rep. | `CF` | `Africa/Bangui` | `UTC+01:00` | No |
| Chad | `TD` | `Africa/Ndjamena` | `UTC+01:00` | No |
| Chile | `CL` | `America/Santiago` | `UTC-04:00` | No |
|  |  | `America/Coyhaique` | `UTC-03:00` | No |
|  |  | `America/Punta_Arenas` | `UTC-03:00` | No |
|  |  | `Pacific/Easter` | `UTC-06:00` | No |
| China | `CN` | `Asia/Shanghai` | `UTC+08:00` | No |
|  |  | `Asia/Urumqi` | `UTC+06:00` | No |
| Christmas Island | `CX` | `Indian/Christmas` | `UTC+07:00` | No |
| Cocos (Keeling) Islands | `CC` | `Indian/Cocos` | `UTC+06:30` | No |
| Colombia | `CO` | `America/Bogota` | `UTC-05:00` | No |
| Comoros | `KM` | `Indian/Comoro` | `UTC+03:00` | No |
| Congo (Dem. Rep.) | `CD` | `Africa/Kinshasa` | `UTC+01:00` | No |
|  |  | `Africa/Lubumbashi` | `UTC+02:00` | No |
| Congo (Rep.) | `CG` | `Africa/Brazzaville` | `UTC+01:00` | No |
| Cook Islands | `CK` | `Pacific/Rarotonga` | `UTC-10:00` | No |
| Costa Rica | `CR` | `America/Costa_Rica` | `UTC-06:00` | No |
| Croatia | `HR` | `Europe/Zagreb` | `UTC+02:00` | Yes |
| Cuba | `CU` | `America/Havana` | `UTC-04:00` | Yes |
| Curaçao | `CW` | `America/Curacao` | `UTC-04:00` | No |
| Cyprus | `CY` | `Asia/Nicosia` | `UTC+03:00` | Yes |
|  |  | `Asia/Famagusta` | `UTC+03:00` | Yes |
| Czech Republic | `CZ` | `Europe/Prague` | `UTC+02:00` | Yes |
| Côte d’Ivoire | `CI` | `Africa/Abidjan` | `UTC+00:00` | No |
| Denmark | `DK` | `Europe/Copenhagen` | `UTC+02:00` | Yes |
| Djibouti | `DJ` | `Africa/Djibouti` | `UTC+03:00` | No |
| Dominica | `DM` | `America/Dominica` | `UTC-04:00` | No |
| Dominican Republic | `DO` | `America/Santo_Domingo` | `UTC-04:00` | No |
| East Timor | `TL` | `Asia/Dili` | `UTC+09:00` | No |
| Ecuador | `EC` | `America/Guayaquil` | `UTC-05:00` | No |
|  |  | `Pacific/Galapagos` | `UTC-06:00` | No |
| Egypt | `EG` | `Africa/Cairo` | `UTC+03:00` | Yes |
| El Salvador | `SV` | `America/El_Salvador` | `UTC-06:00` | No |
| Equatorial Guinea | `GQ` | `Africa/Malabo` | `UTC+01:00` | No |
| Eritrea | `ER` | `Africa/Asmara` | `UTC+03:00` | No |
| Estonia | `EE` | `Europe/Tallinn` | `UTC+03:00` | Yes |
| Eswatini (Swaziland) | `SZ` | `Africa/Mbabane` | `UTC+02:00` | No |
| Ethiopia | `ET` | `Africa/Addis_Ababa` | `UTC+03:00` | No |
| Falkland Islands | `FK` | `Atlantic/Stanley` | `UTC-03:00` | No |
| Faroe Islands | `FO` | `Atlantic/Faroe` | `UTC+01:00` | Yes |
| Fiji | `FJ` | `Pacific/Fiji` | `UTC+12:00` | No |
| Finland | `FI` | `Europe/Helsinki` | `UTC+03:00` | Yes |
| France | `FR` | `Europe/Paris` | `UTC+02:00` | Yes |
| French Guiana | `GF` | `America/Cayenne` | `UTC-03:00` | No |
| French Polynesia | `PF` | `Pacific/Tahiti` | `UTC-10:00` | No |
|  |  | `Pacific/Marquesas` | `UTC-09:30` | No |
|  |  | `Pacific/Gambier` | `UTC-09:00` | No |
| French S. Terr. | `TF` | `Indian/Kerguelen` | `UTC+05:00` | No |
| Gabon | `GA` | `Africa/Libreville` | `UTC+01:00` | No |
| Gambia | `GM` | `Africa/Banjul` | `UTC+00:00` | No |
| Georgia | `GE` | `Asia/Tbilisi` | `UTC+04:00` | No |
| Germany | `DE` | `Europe/Berlin` | `UTC+02:00` | Yes |
|  |  | `Europe/Busingen` | `UTC+02:00` | Yes |
| Ghana | `GH` | `Africa/Accra` | `UTC+00:00` | No |
| Gibraltar | `GI` | `Europe/Gibraltar` | `UTC+02:00` | Yes |
| Greece | `GR` | `Europe/Athens` | `UTC+03:00` | Yes |
| Greenland | `GL` | `America/Nuuk` | `UTC-01:00` | Yes |
|  |  | `America/Danmarkshavn` | `UTC+00:00` | No |
|  |  | `America/Scoresbysund` | `UTC-01:00` | Yes |
|  |  | `America/Thule` | `UTC-03:00` | Yes |
| Grenada | `GD` | `America/Grenada` | `UTC-04:00` | No |
| Guadeloupe | `GP` | `America/Guadeloupe` | `UTC-04:00` | No |
| Guam | `GU` | `Pacific/Guam` | `UTC+10:00` | No |
| Guatemala | `GT` | `America/Guatemala` | `UTC-06:00` | No |
| Guernsey | `GG` | `Europe/Guernsey` | `UTC+01:00` | Yes |
| Guinea | `GN` | `Africa/Conakry` | `UTC+00:00` | No |
| Guinea-Bissau | `GW` | `Africa/Bissau` | `UTC+00:00` | No |
| Guyana | `GY` | `America/Guyana` | `UTC-04:00` | No |
| Haiti | `HT` | `America/Port-au-Prince` | `UTC-04:00` | Yes |
| Honduras | `HN` | `America/Tegucigalpa` | `UTC-06:00` | No |
| Hong Kong | `HK` | `Asia/Hong_Kong` | `UTC+08:00` | No |
| Hungary | `HU` | `Europe/Budapest` | `UTC+02:00` | Yes |
| Iceland | `IS` | `Atlantic/Reykjavik` | `UTC+00:00` | No |
| India | `IN` | `Asia/Kolkata` | `UTC+05:30` | No |
| Indonesia | `ID` | `Asia/Jakarta` | `UTC+07:00` | No |
|  |  | `Asia/Pontianak` | `UTC+07:00` | No |
|  |  | `Asia/Makassar` | `UTC+08:00` | No |
|  |  | `Asia/Jayapura` | `UTC+09:00` | No |
| Iran | `IR` | `Asia/Tehran` | `UTC+03:30` | No |
| Iraq | `IQ` | `Asia/Baghdad` | `UTC+03:00` | No |
| Ireland | `IE` | `Europe/Dublin` | `UTC+01:00` | No |
| Isle of Man | `IM` | `Europe/Isle_of_Man` | `UTC+01:00` | Yes |
| Israel | `IL` | `Asia/Jerusalem` | `UTC+03:00` | Yes |
| Italy | `IT` | `Europe/Rome` | `UTC+02:00` | Yes |
| Jamaica | `JM` | `America/Jamaica` | `UTC-05:00` | No |
| Japan | `JP` | `Asia/Tokyo` | `UTC+09:00` | No |
| Jersey | `JE` | `Europe/Jersey` | `UTC+01:00` | Yes |
| Jordan | `JO` | `Asia/Amman` | `UTC+03:00` | No |
| Kazakhstan | `KZ` | `Asia/Almaty` | `UTC+05:00` | No |
|  |  | `Asia/Qyzylorda` | `UTC+05:00` | No |
|  |  | `Asia/Qostanay` | `UTC+05:00` | No |
|  |  | `Asia/Aqtobe` | `UTC+05:00` | No |
|  |  | `Asia/Aqtau` | `UTC+05:00` | No |
|  |  | `Asia/Atyrau` | `UTC+05:00` | No |
|  |  | `Asia/Oral` | `UTC+05:00` | No |
| Kenya | `KE` | `Africa/Nairobi` | `UTC+03:00` | No |
| Kiribati | `KI` | `Pacific/Tarawa` | `UTC+12:00` | No |
|  |  | `Pacific/Kanton` | `UTC+13:00` | No |
|  |  | `Pacific/Kiritimati` | `UTC+14:00` | No |
| Korea (North) | `KP` | `Asia/Pyongyang` | `UTC+09:00` | No |
| Korea (South) | `KR` | `Asia/Seoul` | `UTC+09:00` | No |
| Kuwait | `KW` | `Asia/Kuwait` | `UTC+03:00` | No |
| Kyrgyzstan | `KG` | `Asia/Bishkek` | `UTC+06:00` | No |
| Laos | `LA` | `Asia/Vientiane` | `UTC+07:00` | No |
| Latvia | `LV` | `Europe/Riga` | `UTC+03:00` | Yes |
| Lebanon | `LB` | `Asia/Beirut` | `UTC+03:00` | Yes |
| Lesotho | `LS` | `Africa/Maseru` | `UTC+02:00` | No |
| Liberia | `LR` | `Africa/Monrovia` | `UTC+00:00` | No |
| Libya | `LY` | `Africa/Tripoli` | `UTC+02:00` | No |
| Liechtenstein | `LI` | `Europe/Vaduz` | `UTC+02:00` | Yes |
| Lithuania | `LT` | `Europe/Vilnius` | `UTC+03:00` | Yes |
| Luxembourg | `LU` | `Europe/Luxembourg` | `UTC+02:00` | Yes |
| Macau | `MO` | `Asia/Macau` | `UTC+08:00` | No |
| Madagascar | `MG` | `Indian/Antananarivo` | `UTC+03:00` | No |
| Malawi | `MW` | `Africa/Blantyre` | `UTC+02:00` | No |
| Malaysia | `MY` | `Asia/Kuala_Lumpur` | `UTC+08:00` | No |
|  |  | `Asia/Kuching` | `UTC+08:00` | No |
| Maldives | `MV` | `Indian/Maldives` | `UTC+05:00` | No |
| Mali | `ML` | `Africa/Bamako` | `UTC+00:00` | No |
| Malta | `MT` | `Europe/Malta` | `UTC+02:00` | Yes |
| Marshall Islands | `MH` | `Pacific/Majuro` | `UTC+12:00` | No |
|  |  | `Pacific/Kwajalein` | `UTC+12:00` | No |
| Martinique | `MQ` | `America/Martinique` | `UTC-04:00` | No |
| Mauritania | `MR` | `Africa/Nouakchott` | `UTC+00:00` | No |
| Mauritius | `MU` | `Indian/Mauritius` | `UTC+04:00` | No |
| Mayotte | `YT` | `Indian/Mayotte` | `UTC+03:00` | No |
| Mexico | `MX` | `America/Mexico_City` | `UTC-06:00` | No |
|  |  | `America/Cancun` | `UTC-05:00` | No |
|  |  | `America/Merida` | `UTC-06:00` | No |
|  |  | `America/Monterrey` | `UTC-06:00` | No |
|  |  | `America/Matamoros` | `UTC-05:00` | Yes |
|  |  | `America/Chihuahua` | `UTC-06:00` | No |
|  |  | `America/Ciudad_Juarez` | `UTC-06:00` | Yes |
|  |  | `America/Ojinaga` | `UTC-05:00` | Yes |
|  |  | `America/Mazatlan` | `UTC-07:00` | No |
|  |  | `America/Bahia_Banderas` | `UTC-06:00` | No |
|  |  | `America/Hermosillo` | `UTC-07:00` | No |
|  |  | `America/Tijuana` | `UTC-07:00` | Yes |
| Micronesia | `FM` | `Pacific/Chuuk` | `UTC+10:00` | No |
|  |  | `Pacific/Pohnpei` | `UTC+11:00` | No |
|  |  | `Pacific/Kosrae` | `UTC+11:00` | No |
| Moldova | `MD` | `Europe/Chisinau` | `UTC+03:00` | Yes |
| Monaco | `MC` | `Europe/Monaco` | `UTC+02:00` | Yes |
| Mongolia | `MN` | `Asia/Ulaanbaatar` | `UTC+08:00` | No |
|  |  | `Asia/Hovd` | `UTC+07:00` | No |
| Montenegro | `ME` | `Europe/Podgorica` | `UTC+02:00` | Yes |
| Montserrat | `MS` | `America/Montserrat` | `UTC-04:00` | No |
| Morocco | `MA` | `Africa/Casablanca` | `UTC+01:00` | No |
| Mozambique | `MZ` | `Africa/Maputo` | `UTC+02:00` | No |
| Myanmar (Burma) | `MM` | `Asia/Yangon` | `UTC+06:30` | No |
| Namibia | `NA` | `Africa/Windhoek` | `UTC+02:00` | No |
| Nauru | `NR` | `Pacific/Nauru` | `UTC+12:00` | No |
| Nepal | `NP` | `Asia/Kathmandu` | `UTC+05:45` | No |
| Netherlands | `NL` | `Europe/Amsterdam` | `UTC+02:00` | Yes |
| New Caledonia | `NC` | `Pacific/Noumea` | `UTC+11:00` | No |
| New Zealand | `NZ` | `Pacific/Auckland` | `UTC+12:00` | No |
|  |  | `Pacific/Chatham` | `UTC+12:45` | No |
| Nicaragua | `NI` | `America/Managua` | `UTC-06:00` | No |
| Niger | `NE` | `Africa/Niamey` | `UTC+01:00` | No |
| Nigeria | `NG` | `Africa/Lagos` | `UTC+01:00` | No |
| Niue | `NU` | `Pacific/Niue` | `UTC-11:00` | No |
| Norfolk Island | `NF` | `Pacific/Norfolk` | `UTC+11:00` | No |
| North Macedonia | `MK` | `Europe/Skopje` | `UTC+02:00` | Yes |
| Northern Mariana Islands | `MP` | `Pacific/Saipan` | `UTC+10:00` | No |
| Norway | `NO` | `Europe/Oslo` | `UTC+02:00` | Yes |
| Oman | `OM` | `Asia/Muscat` | `UTC+04:00` | No |
| Pakistan | `PK` | `Asia/Karachi` | `UTC+05:00` | No |
| Palau | `PW` | `Pacific/Palau` | `UTC+09:00` | No |
| Palestine | `PS` | `Asia/Gaza` | `UTC+03:00` | Yes |
|  |  | `Asia/Hebron` | `UTC+03:00` | Yes |
| Panama | `PA` | `America/Panama` | `UTC-05:00` | No |
| Papua New Guinea | `PG` | `Pacific/Port_Moresby` | `UTC+10:00` | No |
|  |  | `Pacific/Bougainville` | `UTC+11:00` | No |
| Paraguay | `PY` | `America/Asuncion` | `UTC-03:00` | No |
| Peru | `PE` | `America/Lima` | `UTC-05:00` | No |
| Philippines | `PH` | `Asia/Manila` | `UTC+08:00` | No |
| Pitcairn | `PN` | `Pacific/Pitcairn` | `UTC-08:00` | No |
| Poland | `PL` | `Europe/Warsaw` | `UTC+02:00` | Yes |
| Portugal | `PT` | `Europe/Lisbon` | `UTC+01:00` | Yes |
|  |  | `Atlantic/Madeira` | `UTC+01:00` | Yes |
|  |  | `Atlantic/Azores` | `UTC+00:00` | Yes |
| Puerto Rico | `PR` | `America/Puerto_Rico` | `UTC-04:00` | No |
| Qatar | `QA` | `Asia/Qatar` | `UTC+03:00` | No |
| Romania | `RO` | `Europe/Bucharest` | `UTC+03:00` | Yes |
| Russia | `RU` | `Europe/Kaliningrad` | `UTC+02:00` | No |
|  |  | `Europe/Moscow` | `UTC+03:00` | No |
|  |  | `Europe/Kirov` | `UTC+03:00` | No |
|  |  | `Europe/Volgograd` | `UTC+03:00` | No |
|  |  | `Europe/Astrakhan` | `UTC+04:00` | No |
|  |  | `Europe/Saratov` | `UTC+04:00` | No |
|  |  | `Europe/Ulyanovsk` | `UTC+04:00` | No |
|  |  | `Europe/Samara` | `UTC+04:00` | No |
|  |  | `Asia/Yekaterinburg` | `UTC+05:00` | No |
|  |  | `Asia/Omsk` | `UTC+06:00` | No |
|  |  | `Asia/Novosibirsk` | `UTC+07:00` | No |
|  |  | `Asia/Barnaul` | `UTC+07:00` | No |
|  |  | `Asia/Tomsk` | `UTC+07:00` | No |
|  |  | `Asia/Novokuznetsk` | `UTC+07:00` | No |
|  |  | `Asia/Krasnoyarsk` | `UTC+07:00` | No |
|  |  | `Asia/Irkutsk` | `UTC+08:00` | No |
|  |  | `Asia/Chita` | `UTC+09:00` | No |
|  |  | `Asia/Yakutsk` | `UTC+09:00` | No |
|  |  | `Asia/Khandyga` | `UTC+09:00` | No |
|  |  | `Asia/Vladivostok` | `UTC+10:00` | No |
|  |  | `Asia/Ust-Nera` | `UTC+10:00` | No |
|  |  | `Asia/Magadan` | `UTC+11:00` | No |
|  |  | `Asia/Sakhalin` | `UTC+11:00` | No |
|  |  | `Asia/Srednekolymsk` | `UTC+11:00` | No |
|  |  | `Asia/Kamchatka` | `UTC+12:00` | No |
|  |  | `Asia/Anadyr` | `UTC+12:00` | No |
| Rwanda | `RW` | `Africa/Kigali` | `UTC+02:00` | No |
| Réunion | `RE` | `Indian/Reunion` | `UTC+04:00` | No |
| Samoa (American) | `AS` | `Pacific/Pago_Pago` | `UTC-11:00` | No |
| Samoa (western) | `WS` | `Pacific/Apia` | `UTC+13:00` | No |
| San Marino | `SM` | `Europe/San_Marino` | `UTC+02:00` | Yes |
| Sao Tome & Principe | `ST` | `Africa/Sao_Tome` | `UTC+00:00` | No |
| Saudi Arabia | `SA` | `Asia/Riyadh` | `UTC+03:00` | No |
| Senegal | `SN` | `Africa/Dakar` | `UTC+00:00` | No |
| Serbia | `RS` | `Europe/Belgrade` | `UTC+02:00` | Yes |
| Seychelles | `SC` | `Indian/Mahe` | `UTC+04:00` | No |
| Sierra Leone | `SL` | `Africa/Freetown` | `UTC+00:00` | No |
| Singapore | `SG` | `Asia/Singapore` | `UTC+08:00` | No |
| Slovakia | `SK` | `Europe/Bratislava` | `UTC+02:00` | Yes |
| Slovenia | `SI` | `Europe/Ljubljana` | `UTC+02:00` | Yes |
| Solomon Islands | `SB` | `Pacific/Guadalcanal` | `UTC+11:00` | No |
| Somalia | `SO` | `Africa/Mogadishu` | `UTC+03:00` | No |
| South Africa | `ZA` | `Africa/Johannesburg` | `UTC+02:00` | No |
| South Georgia & the South Sandwich Islands | `GS` | `Atlantic/South_Georgia` | `UTC-02:00` | No |
| South Sudan | `SS` | `Africa/Juba` | `UTC+02:00` | No |
| Spain | `ES` | `Europe/Madrid` | `UTC+02:00` | Yes |
|  |  | `Africa/Ceuta` | `UTC+02:00` | Yes |
|  |  | `Atlantic/Canary` | `UTC+01:00` | Yes |
| Sri Lanka | `LK` | `Asia/Colombo` | `UTC+05:30` | No |
| St Barthelemy | `BL` | `America/St_Barthelemy` | `UTC-04:00` | No |
| St Helena | `SH` | `Atlantic/St_Helena` | `UTC+00:00` | No |
| St Kitts & Nevis | `KN` | `America/St_Kitts` | `UTC-04:00` | No |
| St Lucia | `LC` | `America/St_Lucia` | `UTC-04:00` | No |
| St Maarten (Dutch) | `SX` | `America/Lower_Princes` | `UTC-04:00` | No |
| St Martin (French) | `MF` | `America/Marigot` | `UTC-04:00` | No |
| St Pierre & Miquelon | `PM` | `America/Miquelon` | `UTC-02:00` | Yes |
| St Vincent | `VC` | `America/St_Vincent` | `UTC-04:00` | No |
| Sudan | `SD` | `Africa/Khartoum` | `UTC+02:00` | No |
| Suriname | `SR` | `America/Paramaribo` | `UTC-03:00` | No |
| Svalbard & Jan Mayen | `SJ` | `Arctic/Longyearbyen` | `UTC+02:00` | Yes |
| Sweden | `SE` | `Europe/Stockholm` | `UTC+02:00` | Yes |
| Switzerland | `CH` | `Europe/Zurich` | `UTC+02:00` | Yes |
| Syria | `SY` | `Asia/Damascus` | `UTC+03:00` | No |
| Taiwan | `TW` | `Asia/Taipei` | `UTC+08:00` | No |
| Tajikistan | `TJ` | `Asia/Dushanbe` | `UTC+05:00` | No |
| Tanzania | `TZ` | `Africa/Dar_es_Salaam` | `UTC+03:00` | No |
| Thailand | `TH` | `Asia/Bangkok` | `UTC+07:00` | No |
| Togo | `TG` | `Africa/Lome` | `UTC+00:00` | No |
| Tokelau | `TK` | `Pacific/Fakaofo` | `UTC+13:00` | No |
| Tonga | `TO` | `Pacific/Tongatapu` | `UTC+13:00` | No |
| Trinidad & Tobago | `TT` | `America/Port_of_Spain` | `UTC-04:00` | No |
| Tunisia | `TN` | `Africa/Tunis` | `UTC+01:00` | No |
| Turkey | `TR` | `Europe/Istanbul` | `UTC+03:00` | No |
| Turkmenistan | `TM` | `Asia/Ashgabat` | `UTC+05:00` | No |
| Turks & Caicos Is | `TC` | `America/Grand_Turk` | `UTC-04:00` | Yes |
| Tuvalu | `TV` | `Pacific/Funafuti` | `UTC+12:00` | No |
| US minor outlying islands | `UM` | `Pacific/Midway` | `UTC-11:00` | No |
|  |  | `Pacific/Wake` | `UTC+12:00` | No |
| Uganda | `UG` | `Africa/Kampala` | `UTC+03:00` | No |
| Ukraine | `UA` | `Europe/Simferopol` | `UTC+03:00` | No |
|  |  | `Europe/Kyiv` | `UTC+03:00` | Yes |
| United Arab Emirates | `AE` | `Asia/Dubai` | `UTC+04:00` | No |
| United States | `US` | `America/New_York` | `UTC-04:00` | Yes |
|  |  | `America/Detroit` | `UTC-04:00` | Yes |
|  |  | `America/Kentucky/Louisville` | `UTC-04:00` | Yes |
|  |  | `America/Kentucky/Monticello` | `UTC-04:00` | Yes |
|  |  | `America/Indiana/Indianapolis` | `UTC-04:00` | Yes |
|  |  | `America/Indiana/Vincennes` | `UTC-04:00` | Yes |
|  |  | `America/Indiana/Winamac` | `UTC-04:00` | Yes |
|  |  | `America/Indiana/Marengo` | `UTC-04:00` | Yes |
|  |  | `America/Indiana/Petersburg` | `UTC-04:00` | Yes |
|  |  | `America/Indiana/Vevay` | `UTC-04:00` | Yes |
|  |  | `America/Chicago` | `UTC-05:00` | Yes |
|  |  | `America/Indiana/Tell_City` | `UTC-05:00` | Yes |
|  |  | `America/Indiana/Knox` | `UTC-05:00` | Yes |
|  |  | `America/Menominee` | `UTC-05:00` | Yes |
|  |  | `America/North_Dakota/Center` | `UTC-05:00` | Yes |
|  |  | `America/North_Dakota/New_Salem` | `UTC-05:00` | Yes |
|  |  | `America/North_Dakota/Beulah` | `UTC-05:00` | Yes |
|  |  | `America/Denver` | `UTC-06:00` | Yes |
|  |  | `America/Boise` | `UTC-06:00` | Yes |
|  |  | `America/Phoenix` | `UTC-07:00` | No |
|  |  | `America/Los_Angeles` | `UTC-07:00` | Yes |
|  |  | `America/Anchorage` | `UTC-08:00` | Yes |
|  |  | `America/Juneau` | `UTC-08:00` | Yes |
|  |  | `America/Sitka` | `UTC-08:00` | Yes |
|  |  | `America/Metlakatla` | `UTC-08:00` | Yes |
|  |  | `America/Yakutat` | `UTC-08:00` | Yes |
|  |  | `America/Nome` | `UTC-08:00` | Yes |
|  |  | `America/Adak` | `UTC-09:00` | Yes |
|  |  | `Pacific/Honolulu` | `UTC-10:00` | No |
| Uruguay | `UY` | `America/Montevideo` | `UTC-03:00` | No |
| Uzbekistan | `UZ` | `Asia/Samarkand` | `UTC+05:00` | No |
|  |  | `Asia/Tashkent` | `UTC+05:00` | No |
| Vanuatu | `VU` | `Pacific/Efate` | `UTC+11:00` | No |
| Vatican City | `VA` | `Europe/Vatican` | `UTC+02:00` | Yes |
| Venezuela | `VE` | `America/Caracas` | `UTC-04:00` | No |
| Vietnam | `VN` | `Asia/Ho_Chi_Minh` | `UTC+07:00` | No |
| Virgin Islands (UK) | `VG` | `America/Tortola` | `UTC-04:00` | No |
| Virgin Islands (US) | `VI` | `America/St_Thomas` | `UTC-04:00` | No |
| Wallis & Futuna | `WF` | `Pacific/Wallis` | `UTC+12:00` | No |
| Western Sahara | `EH` | `Africa/El_Aaiun` | `UTC+01:00` | No |
| Yemen | `YE` | `Asia/Aden` | `UTC+03:00` | No |
| Zambia | `ZM` | `Africa/Lusaka` | `UTC+02:00` | No |
| Zimbabwe | `ZW` | `Africa/Harare` | `UTC+02:00` | No |
| Åland Islands | `AX` | `Europe/Mariehamn` | `UTC+03:00` | Yes |

## Author

Developed by [Ramazan Çetinkaya](https://github.com/ramazancetinkaya)

## License

Distributed under the MIT License. See [LICENSE](./LICENSE) for details.
