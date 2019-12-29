import pytest
from pytest import approx
from datetime import datetime
import pymap3d as pm

lat, lon = (65, -148)
lla0 = (42, -82, 200)
azel = (180.1, 80)
t0 = datetime(2014, 4, 6, 8)
radec = (166.5032081149338, 55.000011165405752)


@pytest.mark.parametrize("usevallado", [True, False])
def test_azel2radec(usevallado):
    radec1 = pm.azel2radec(*azel, lat, lon, t0, usevallado=usevallado)
    assert radec1 == approx(radec, rel=0.01)


@pytest.mark.parametrize("usevallado", [True, False])
def test_numpy_azel2radec(usevallado):
    pytest.importorskip("numpy")
    radec1 = pm.azel2radec([180.1, 180.1], [80, 80], lat, lon, t0, usevallado=usevallado)
    assert radec1 == approx(radec, rel=0.01)


@pytest.mark.parametrize("usevallado", [True, False])
def test_radec2azel(usevallado):
    azel1 = pm.radec2azel(*radec, lat, lon, t0, usevallado=usevallado)
    assert azel1 == approx(azel, rel=0.01)


@pytest.mark.parametrize("usevallado", [True, False])
def test_numpy_radec2azel(usevallado):
    pytest.importorskip("numpy")
    azel1 = pm.radec2azel([166.503208, 166.503208], [55, 55], lat, lon, t0, usevallado=usevallado)
    assert azel1 == approx(azel, rel=0.01)


if __name__ == "__main__":
    pytest.main([__file__])
