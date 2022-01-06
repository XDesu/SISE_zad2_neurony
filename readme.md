# SISE - Badania nad poprawą lokalizacji UWB przy pomocy sieci neuronowych

# autorzy
> - Adam Kapuściński 229907
> - Damian Szczeciński 230016

# struktura słownika z danymi
```
data[<room>][<type>][<direction>][<file_number>][<row>][<col_name>]
```

> room - `f8` | `f10` \
> type - `dynamic` | `static` | `random` \
> direction - `p` | `z` | `s` \
> file_number - numer porządkowy - 1 (indeksowanie od `0`) \
> row - równe kolumnie `Unnamed: 1` \
> col_name - kolumna w excelu

# dostępne kolumny w excelu
None, \
'Unnamed: 0', \
'version', \
'alive', \
'tagId', \
'success', \
'timestamp', \
'data__tagData__gyro__x', \
'data__tagData__gyro__y', \
'data__tagData__gyro__z', \
'data__tagData__magnetic__x', \
'data__tagData__magnetic__y', \
'data__tagData__magnetic__z', \
'data__tagData__quaternion__x', \
'data__tagData__quaternion__y', \
'data__tagData__quaternion__z', \
'data__tagData__quaternion__w', \
'data__tagData__linearAcceleration__x', \
'data__tagData__linearAcceleration__y', \
'data__tagData__linearAcceleration__z', \
'data__tagData__pressure', \
'data__tagData__maxLinearAcceleration', \
'data__anchorData', \
'data__acceleration__x', \
'data__acceleration__y', \
'data__acceleration__z', \
'data__orientation__yaw', \
'data__orientation__roll', \
'data__orientation__pitch', \
'data__metrics__latency', \
'data__metrics__rates__update', \
'data__metrics__rates__success', \
'data__coordinates__x', \
'data__coordinates__y', \
'data__coordinates__z', \
'errorCode', \
'reference__x', \
'reference__y'