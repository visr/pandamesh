import abc
from typing import Tuple

import geopandas as gpd

from pandamesh.common import FloatArray, IntArray, to_geodataframe, to_ugrid


class MesherBase(abc.ABC):
    @abc.abstractmethod
    def generate(self) -> Tuple[FloatArray, IntArray]:
        pass

    def generate_geodataframe(self) -> gpd.GeoDataFrame:
        """
        Generate a mesh and return it as a geopandas GeoDataFrame.

        Returns
        -------
        mesh: geopandas.GeoDataFrame
        """
        return to_geodataframe(*self.generate())

    def generate_ugrid(self) -> "xugrid.Ugrid2d":  # type: ignore # noqa  pragma: no cover
        """
        Generate a mesh and return it as an xugrid Ugrid2d.

        Returns
        -------
        mesh: xugrid.Ugrid2d
        """
        return to_ugrid(*self.generate())
