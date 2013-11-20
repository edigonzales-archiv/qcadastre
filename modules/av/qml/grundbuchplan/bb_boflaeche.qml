<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis version="2.1.0-Master" minimumScale="0" maximumScale="25000" minLabelScale="1" maxLabelScale="1e+08" hasScaleBasedVisibilityFlag="1" scaleBasedLabelVisibilityFlag="0">
  <renderer-v2 symbollevels="0" type="RuleRenderer">
    <rules>
      <rule filter="&quot;art_txt&quot; LIKE 'befestigt.Bahn%' OR &quot;art_txt&quot; LIKE 'befestigt.uebrige_befestigte%' OR &quot;art_txt&quot; LIKE 'humusiert%' OR &quot;art_txt&quot; LIKE 'Gewaesser.Schilfguertel%' OR &quot;art_txt&quot; LIKE 'bestockt%' OR &quot;art_txt&quot; LIKE 'vegetationslos%'" label="gestrichelt">
        <rule scalemaxdenom="300" symbol="0" label="1:250"/>
        <rule scalemaxdenom="750" symbol="1" scalemindenom="300" label="1:500"/>
        <rule scalemaxdenom="1250" symbol="2" scalemindenom="750" label="1:1000"/>
        <rule scalemaxdenom="3000" symbol="3" scalemindenom="1250" label="1:2000"/>
        <rule scalemaxdenom="6000" symbol="4" scalemindenom="3000" label="1:5000"/>
        <rule scalemaxdenom="25000" filter="&quot;art_txt&quot; LIKE 'bestockt.geschlossener_Wald%'" symbol="5" scalemindenom="6000" label="> 1:5000"/>
      </rule>
      <rule filter="&quot;art_txt&quot; LIKE 'Gebaeude' OR &quot;art_txt&quot; LIKE 'befestigt.Strasse_Weg%' OR &quot;art_txt&quot; LIKE 'befestigt.Trottoir%' OR &quot;art_txt&quot; LIKE 'befestigt.Verkehrsinsel%' OR &quot;art_txt&quot; LIKE 'befestigt.Flugplatz%' OR &quot;art_txt&quot; LIKE 'befestigt.Wasserbecken%' OR &quot;art_txt&quot; LIKE 'Gewaesser.stehendes%' OR &quot;art_txt&quot; LIKE 'Gewaesser.fliessendes%'" label="ausgezogen">
        <rule scalemaxdenom="300" symbol="6" label="1:250"/>
        <rule scalemaxdenom="750" symbol="7" scalemindenom="300" label="1:500"/>
        <rule scalemaxdenom="1250" symbol="8" scalemindenom="750" label="1:1000"/>
        <rule scalemaxdenom="3000" symbol="9" scalemindenom="1250" label="1:2000"/>
        <rule scalemaxdenom="6000" symbol="10" scalemindenom="3000" label="1:5000"/>
        <rule scalemaxdenom="25000" filter="&quot;art_txt&quot; LIKE 'Gebaeude%' OR &quot;art_txt&quot; LIKE 'befestigt.Strasse_Weg%'" symbol="11" scalemindenom="6000" label="> 1:5000"/>
      </rule>
      <rule filter="&quot;art_txt&quot; LIKE 'Gebaeude%'" symbol="12" label="Gebaeude"/>
      <rule filter="&quot;art_txt&quot; LIKE 'humusiert.Intensivkultur.Reben%'" label="Reben">
        <rule scalemaxdenom="300" symbol="13" label="1:250"/>
        <rule scalemaxdenom="750" symbol="14" scalemindenom="300" label="1:500"/>
        <rule scalemaxdenom="1250" symbol="15" scalemindenom="750" label="1:1000"/>
        <rule scalemaxdenom="3000" symbol="16" scalemindenom="1250" label="1:2000"/>
        <rule scalemaxdenom="6000" symbol="17" scalemindenom="3000" label="1:5000"/>
      </rule>
      <rule filter="&quot;art_txt&quot; LIKE 'humusiert.Hoch_Flachmoor%'" label="Moor">
        <rule scalemaxdenom="300" symbol="18" label="1:250"/>
        <rule scalemaxdenom="750" symbol="19" scalemindenom="300" label="1:500"/>
        <rule scalemaxdenom="1250" symbol="20" scalemindenom="750" label="1:1000"/>
        <rule scalemaxdenom="3000" symbol="21" scalemindenom="1250" label="1:2000"/>
        <rule scalemaxdenom="6000" symbol="22" scalemindenom="3000" label="1:5000"/>
      </rule>
      <rule filter="&quot;art_txt&quot; LIKE 'Gewaesser.Schilfguertel%'" label="Schilfguertel">
        <rule scalemaxdenom="300" symbol="23" label="1:250"/>
        <rule scalemaxdenom="750" symbol="24" scalemindenom="300" label="1:500"/>
        <rule scalemaxdenom="1250" symbol="25" scalemindenom="750" label="1:1000"/>
        <rule scalemaxdenom="3000" symbol="26" scalemindenom="1250" label="1:2000"/>
        <rule scalemaxdenom="6000" symbol="27" scalemindenom="3000" label="1:5000"/>
      </rule>
      <rule filter="&quot;art_txt&quot; LIKE 'bestockt.geschlossener_Wald%'" label="geschlossener_Wald">
        <rule scalemaxdenom="300" symbol="28" label="1:250"/>
        <rule scalemaxdenom="750" symbol="29" scalemindenom="300" label="1:500"/>
        <rule scalemaxdenom="1250" symbol="30" scalemindenom="750" label="1:1000"/>
        <rule scalemaxdenom="3000" symbol="31" scalemindenom="1250" label="1:2000"/>
        <rule scalemaxdenom="25000" symbol="32" scalemindenom="3000" label="1:5000"/>
      </rule>
      <rule filter="&quot;art_txt&quot; = 'bestockt.uebrige_bestockte%'" label="uebrige_bestockte">
        <rule scalemaxdenom="300" symbol="33" label="1:250"/>
        <rule scalemaxdenom="750" symbol="34" scalemindenom="300" label="1:500"/>
        <rule scalemaxdenom="1250" symbol="35" scalemindenom="750" label="1:1000"/>
        <rule scalemaxdenom="3000" symbol="36" scalemindenom="1250" label="1:2000"/>
        <rule scalemaxdenom="6000" symbol="37" scalemindenom="3000" label="1:5000"/>
      </rule>
      <rule filter="&quot;art_txt&quot; LIKE 'vegetationslos.Fels%'" label="Fels">
        <rule scalemaxdenom="300" symbol="38" label="1:250"/>
        <rule scalemaxdenom="750" symbol="39" scalemindenom="300" label="1:500"/>
        <rule scalemaxdenom="1250" symbol="40" scalemindenom="750" label="1:1000"/>
        <rule scalemaxdenom="3000" symbol="41" scalemindenom="1250" label="1:2000"/>
        <rule scalemaxdenom="6000" symbol="42" scalemindenom="3000" label="1:5000"/>
      </rule>
      <rule filter="&quot;art_txt&quot; LIKE 'vegetationslos.Geroell_Sand%'" label="Geröll_Sand">
        <rule scalemaxdenom="300" symbol="43" label="1:250"/>
        <rule scalemaxdenom="750" symbol="44" scalemindenom="300" label="1:500"/>
        <rule scalemaxdenom="1250" symbol="45" scalemindenom="750" label="1:1000"/>
        <rule scalemaxdenom="3000" symbol="46" scalemindenom="1250" label="1:2000"/>
        <rule scalemaxdenom="5000" symbol="47" scalemindenom="3000" label="1:5000"/>
      </rule>
    </rules>
    <symbols>
      <symbol alpha="1" type="fill" name="0">
        <layer pass="90" class="SimpleLine" locked="0">
          <prop k="capstyle" v="square"/>
          <prop k="color" v="255,255,255,255"/>
          <prop k="customdash" v="5;2"/>
          <prop k="customdash_unit" v="MM"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="penstyle" v="solid"/>
          <prop k="use_custom_dash" v="0"/>
          <prop k="width" v="0.34"/>
          <prop k="width_unit" v="MM"/>
        </layer>
        <layer pass="90" class="SimpleLine" locked="0">
          <prop k="capstyle" v="flat"/>
          <prop k="color" v="0,0,0,255"/>
          <prop k="customdash" v="2.1;0.7"/>
          <prop k="customdash_unit" v="MM"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="penstyle" v="solid"/>
          <prop k="use_custom_dash" v="1"/>
          <prop k="width" v="0.28"/>
          <prop k="width_unit" v="MM"/>
        </layer>
      </symbol>
      <symbol alpha="1" type="fill" name="1">
        <layer pass="90" class="SimpleLine" locked="0">
          <prop k="capstyle" v="square"/>
          <prop k="color" v="255,255,255,255"/>
          <prop k="customdash" v="5;2"/>
          <prop k="customdash_unit" v="MM"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="penstyle" v="solid"/>
          <prop k="use_custom_dash" v="0"/>
          <prop k="width" v="0.34"/>
          <prop k="width_unit" v="MM"/>
        </layer>
        <layer pass="90" class="SimpleLine" locked="0">
          <prop k="capstyle" v="flat"/>
          <prop k="color" v="0,0,0,255"/>
          <prop k="customdash" v="2.1;0.7"/>
          <prop k="customdash_unit" v="MM"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="penstyle" v="solid"/>
          <prop k="use_custom_dash" v="1"/>
          <prop k="width" v="0.28"/>
          <prop k="width_unit" v="MM"/>
        </layer>
      </symbol>
      <symbol alpha="1" type="fill" name="10">
        <layer pass="99" class="SimpleLine" locked="0">
          <prop k="capstyle" v="square"/>
          <prop k="color" v="255,255,255,255"/>
          <prop k="customdash" v="5;2"/>
          <prop k="customdash_unit" v="MM"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="penstyle" v="solid"/>
          <prop k="use_custom_dash" v="0"/>
          <prop k="width" v="0.15"/>
          <prop k="width_unit" v="MM"/>
        </layer>
        <layer pass="99" class="SimpleLine" locked="0">
          <prop k="capstyle" v="flat"/>
          <prop k="color" v="0,0,0,255"/>
          <prop k="customdash" v="1.5;0.5"/>
          <prop k="customdash_unit" v="MM"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="penstyle" v="solid"/>
          <prop k="use_custom_dash" v="0"/>
          <prop k="width" v="0.1"/>
          <prop k="width_unit" v="MM"/>
        </layer>
      </symbol>
      <symbol alpha="1" type="fill" name="11">
        <layer pass="99" class="SimpleLine" locked="0">
          <prop k="capstyle" v="square"/>
          <prop k="color" v="255,255,255,255"/>
          <prop k="customdash" v="5;2"/>
          <prop k="customdash_unit" v="MM"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="penstyle" v="solid"/>
          <prop k="use_custom_dash" v="0"/>
          <prop k="width" v="0.15"/>
          <prop k="width_unit" v="MM"/>
        </layer>
        <layer pass="99" class="SimpleLine" locked="0">
          <prop k="capstyle" v="flat"/>
          <prop k="color" v="0,0,0,255"/>
          <prop k="customdash" v="1.5;0.5"/>
          <prop k="customdash_unit" v="MM"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="penstyle" v="solid"/>
          <prop k="use_custom_dash" v="0"/>
          <prop k="width" v="0.1"/>
          <prop k="width_unit" v="MM"/>
        </layer>
      </symbol>
      <symbol alpha="1" type="fill" name="12">
        <layer pass="95" class="SimpleFill" locked="0">
          <prop k="border_width_unit" v="MM"/>
          <prop k="color" v="178,178,178,255"/>
          <prop k="color_border" v="0,0,0,255"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="style" v="solid"/>
          <prop k="style_border" v="no"/>
          <prop k="width_border" v="0.26"/>
        </layer>
      </symbol>
      <symbol alpha="1" type="fill" name="13">
        <layer pass="0" class="PointPatternFill" locked="0">
          <prop k="displacement_x" v="7"/>
          <prop k="displacement_x_unit" v="MM"/>
          <prop k="displacement_y" v="0"/>
          <prop k="displacement_y_unit" v="MM"/>
          <prop k="distance_x" v="14"/>
          <prop k="distance_x_unit" v="MM"/>
          <prop k="distance_y" v="14"/>
          <prop k="distance_y_unit" v="MM"/>
          <symbol alpha="1" type="marker" name="@13@0">
            <layer pass="0" class="SvgMarker" locked="0">
              <prop k="angle" v="0"/>
              <prop k="fill" v="#828282"/>
              <prop k="horizontal_anchor_point" v="1"/>
              <prop k="name" v="/grundbuchplan/symbol_b_reben_param.svg"/>
              <prop k="offset" v="0,0"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="outline" v="#000000"/>
              <prop k="outline-width" v="1"/>
              <prop k="outline_width_unit" v="MM"/>
              <prop k="size" v="4.2"/>
              <prop k="size_unit" v="MM"/>
              <prop k="vertical_anchor_point" v="1"/>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol alpha="1" type="fill" name="14">
        <layer pass="0" class="PointPatternFill" locked="0">
          <prop k="displacement_x" v="7"/>
          <prop k="displacement_x_unit" v="MM"/>
          <prop k="displacement_y" v="0"/>
          <prop k="displacement_y_unit" v="MM"/>
          <prop k="distance_x" v="14"/>
          <prop k="distance_x_unit" v="MM"/>
          <prop k="distance_y" v="14"/>
          <prop k="distance_y_unit" v="MM"/>
          <symbol alpha="1" type="marker" name="@14@0">
            <layer pass="0" class="SvgMarker" locked="0">
              <prop k="angle" v="0"/>
              <prop k="fill" v="#828282"/>
              <prop k="horizontal_anchor_point" v="1"/>
              <prop k="name" v="/grundbuchplan/symbol_b_reben_param.svg"/>
              <prop k="offset" v="0,0"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="outline" v="#000000"/>
              <prop k="outline-width" v="1"/>
              <prop k="outline_width_unit" v="MM"/>
              <prop k="size" v="4.2"/>
              <prop k="size_unit" v="MM"/>
              <prop k="vertical_anchor_point" v="1"/>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol alpha="1" type="fill" name="15">
        <layer pass="0" class="PointPatternFill" locked="0">
          <prop k="displacement_x" v="5"/>
          <prop k="displacement_x_unit" v="MM"/>
          <prop k="displacement_y" v="0"/>
          <prop k="displacement_y_unit" v="MM"/>
          <prop k="distance_x" v="10"/>
          <prop k="distance_x_unit" v="MM"/>
          <prop k="distance_y" v="10"/>
          <prop k="distance_y_unit" v="MM"/>
          <symbol alpha="1" type="marker" name="@15@0">
            <layer pass="0" class="SvgMarker" locked="0">
              <prop k="angle" v="0"/>
              <prop k="fill" v="#828282"/>
              <prop k="horizontal_anchor_point" v="1"/>
              <prop k="name" v="/grundbuchplan/symbol_b_reben_param.svg"/>
              <prop k="offset" v="0,0"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="outline" v="#000000"/>
              <prop k="outline-width" v="1"/>
              <prop k="outline_width_unit" v="MM"/>
              <prop k="size" v="3"/>
              <prop k="size_unit" v="MM"/>
              <prop k="vertical_anchor_point" v="1"/>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol alpha="1" type="fill" name="16">
        <layer pass="0" class="PointPatternFill" locked="0">
          <prop k="displacement_x" v="3.5"/>
          <prop k="displacement_x_unit" v="MM"/>
          <prop k="displacement_y" v="0"/>
          <prop k="displacement_y_unit" v="MM"/>
          <prop k="distance_x" v="7"/>
          <prop k="distance_x_unit" v="MM"/>
          <prop k="distance_y" v="7"/>
          <prop k="distance_y_unit" v="MM"/>
          <symbol alpha="1" type="marker" name="@16@0">
            <layer pass="0" class="SvgMarker" locked="0">
              <prop k="angle" v="0"/>
              <prop k="fill" v="#828282"/>
              <prop k="horizontal_anchor_point" v="1"/>
              <prop k="name" v="/grundbuchplan/symbol_b_reben_param.svg"/>
              <prop k="offset" v="0,0"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="outline" v="#000000"/>
              <prop k="outline-width" v="1"/>
              <prop k="outline_width_unit" v="MM"/>
              <prop k="size" v="2.1"/>
              <prop k="size_unit" v="MM"/>
              <prop k="vertical_anchor_point" v="1"/>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol alpha="1" type="fill" name="17">
        <layer pass="0" class="PointPatternFill" locked="0">
          <prop k="displacement_x" v="2.45"/>
          <prop k="displacement_x_unit" v="MM"/>
          <prop k="displacement_y" v="0"/>
          <prop k="displacement_y_unit" v="MM"/>
          <prop k="distance_x" v="4.9"/>
          <prop k="distance_x_unit" v="MM"/>
          <prop k="distance_y" v="4.9"/>
          <prop k="distance_y_unit" v="MM"/>
          <symbol alpha="1" type="marker" name="@17@0">
            <layer pass="0" class="SvgMarker" locked="0">
              <prop k="angle" v="0"/>
              <prop k="fill" v="#828282"/>
              <prop k="horizontal_anchor_point" v="1"/>
              <prop k="name" v="/grundbuchplan/symbol_b_reben_param.svg"/>
              <prop k="offset" v="0,0"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="outline" v="#000000"/>
              <prop k="outline-width" v="1"/>
              <prop k="outline_width_unit" v="MM"/>
              <prop k="size" v="1.5"/>
              <prop k="size_unit" v="MM"/>
              <prop k="vertical_anchor_point" v="1"/>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol alpha="1" type="fill" name="18">
        <layer pass="0" class="PointPatternFill" locked="0">
          <prop k="displacement_x" v="7"/>
          <prop k="displacement_x_unit" v="MM"/>
          <prop k="displacement_y" v="0"/>
          <prop k="displacement_y_unit" v="MM"/>
          <prop k="distance_x" v="14"/>
          <prop k="distance_x_unit" v="MM"/>
          <prop k="distance_y" v="14"/>
          <prop k="distance_y_unit" v="MM"/>
          <symbol alpha="1" type="marker" name="@18@0">
            <layer pass="0" class="SvgMarker" locked="0">
              <prop k="angle" v="0"/>
              <prop k="fill" v="#828282"/>
              <prop k="horizontal_anchor_point" v="1"/>
              <prop k="name" v="/grundbuchplan/symbol_d_moor_param.svg"/>
              <prop k="offset" v="0,0"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="outline" v="#000000"/>
              <prop k="outline-width" v="1"/>
              <prop k="outline_width_unit" v="MM"/>
              <prop k="size" v="5.6"/>
              <prop k="size_unit" v="MM"/>
              <prop k="vertical_anchor_point" v="1"/>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol alpha="1" type="fill" name="19">
        <layer pass="0" class="PointPatternFill" locked="0">
          <prop k="displacement_x" v="7"/>
          <prop k="displacement_x_unit" v="MM"/>
          <prop k="displacement_y" v="0"/>
          <prop k="displacement_y_unit" v="MM"/>
          <prop k="distance_x" v="14"/>
          <prop k="distance_x_unit" v="MM"/>
          <prop k="distance_y" v="14"/>
          <prop k="distance_y_unit" v="MM"/>
          <symbol alpha="1" type="marker" name="@19@0">
            <layer pass="0" class="SvgMarker" locked="0">
              <prop k="angle" v="0"/>
              <prop k="fill" v="#828282"/>
              <prop k="horizontal_anchor_point" v="1"/>
              <prop k="name" v="/grundbuchplan/symbol_d_moor_param.svg"/>
              <prop k="offset" v="0,0"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="outline" v="#000000"/>
              <prop k="outline-width" v="1"/>
              <prop k="outline_width_unit" v="MM"/>
              <prop k="size" v="5.6"/>
              <prop k="size_unit" v="MM"/>
              <prop k="vertical_anchor_point" v="1"/>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol alpha="1" type="fill" name="2">
        <layer pass="90" class="SimpleLine" locked="0">
          <prop k="capstyle" v="square"/>
          <prop k="color" v="255,255,255,255"/>
          <prop k="customdash" v="5;2"/>
          <prop k="customdash_unit" v="MM"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="penstyle" v="solid"/>
          <prop k="use_custom_dash" v="0"/>
          <prop k="width" v="0.3"/>
          <prop k="width_unit" v="MM"/>
        </layer>
        <layer pass="90" class="SimpleLine" locked="0">
          <prop k="capstyle" v="flat"/>
          <prop k="color" v="0,0,0,255"/>
          <prop k="customdash" v="1.5;0.5"/>
          <prop k="customdash_unit" v="MM"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="penstyle" v="solid"/>
          <prop k="use_custom_dash" v="1"/>
          <prop k="width" v="0.2"/>
          <prop k="width_unit" v="MM"/>
        </layer>
      </symbol>
      <symbol alpha="1" type="fill" name="20">
        <layer pass="0" class="PointPatternFill" locked="0">
          <prop k="displacement_x" v="5"/>
          <prop k="displacement_x_unit" v="MM"/>
          <prop k="displacement_y" v="0"/>
          <prop k="displacement_y_unit" v="MM"/>
          <prop k="distance_x" v="10"/>
          <prop k="distance_x_unit" v="MM"/>
          <prop k="distance_y" v="10"/>
          <prop k="distance_y_unit" v="MM"/>
          <symbol alpha="1" type="marker" name="@20@0">
            <layer pass="0" class="SvgMarker" locked="0">
              <prop k="angle" v="0"/>
              <prop k="fill" v="#828282"/>
              <prop k="horizontal_anchor_point" v="1"/>
              <prop k="name" v="/grundbuchplan/symbol_d_moor_param.svg"/>
              <prop k="offset" v="0,0"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="outline" v="#000000"/>
              <prop k="outline-width" v="1"/>
              <prop k="outline_width_unit" v="MM"/>
              <prop k="size" v="4"/>
              <prop k="size_unit" v="MM"/>
              <prop k="vertical_anchor_point" v="1"/>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol alpha="1" type="fill" name="21">
        <layer pass="0" class="PointPatternFill" locked="0">
          <prop k="displacement_x" v="2.45"/>
          <prop k="displacement_x_unit" v="MM"/>
          <prop k="displacement_y" v="0"/>
          <prop k="displacement_y_unit" v="MM"/>
          <prop k="distance_x" v="4.9"/>
          <prop k="distance_x_unit" v="MM"/>
          <prop k="distance_y" v="4.9"/>
          <prop k="distance_y_unit" v="MM"/>
          <symbol alpha="1" type="marker" name="@21@0">
            <layer pass="0" class="SvgMarker" locked="0">
              <prop k="angle" v="0"/>
              <prop k="fill" v="#828282"/>
              <prop k="horizontal_anchor_point" v="1"/>
              <prop k="name" v="/grundbuchplan/symbol_b_reben_param.svg"/>
              <prop k="offset" v="0,0"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="outline" v="#000000"/>
              <prop k="outline-width" v="1"/>
              <prop k="outline_width_unit" v="MM"/>
              <prop k="size" v="1.5"/>
              <prop k="size_unit" v="MM"/>
              <prop k="vertical_anchor_point" v="1"/>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol alpha="1" type="fill" name="22">
        <layer pass="0" class="PointPatternFill" locked="0">
          <prop k="displacement_x" v="2.45"/>
          <prop k="displacement_x_unit" v="MM"/>
          <prop k="displacement_y" v="0"/>
          <prop k="displacement_y_unit" v="MM"/>
          <prop k="distance_x" v="4.9"/>
          <prop k="distance_x_unit" v="MM"/>
          <prop k="distance_y" v="4.9"/>
          <prop k="distance_y_unit" v="MM"/>
          <symbol alpha="1" type="marker" name="@22@0">
            <layer pass="0" class="SvgMarker" locked="0">
              <prop k="angle" v="0"/>
              <prop k="fill" v="#828282"/>
              <prop k="horizontal_anchor_point" v="1"/>
              <prop k="name" v="/grundbuchplan/symbol_d_moor_param.svg"/>
              <prop k="offset" v="0,0"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="outline" v="#000000"/>
              <prop k="outline-width" v="1"/>
              <prop k="outline_width_unit" v="MM"/>
              <prop k="size" v="2"/>
              <prop k="size_unit" v="MM"/>
              <prop k="vertical_anchor_point" v="1"/>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol alpha="1" type="fill" name="23">
        <layer pass="0" class="PointPatternFill" locked="0">
          <prop k="displacement_x" v="7"/>
          <prop k="displacement_x_unit" v="MM"/>
          <prop k="displacement_y" v="0"/>
          <prop k="displacement_y_unit" v="MM"/>
          <prop k="distance_x" v="14"/>
          <prop k="distance_x_unit" v="MM"/>
          <prop k="distance_y" v="14"/>
          <prop k="distance_y_unit" v="MM"/>
          <symbol alpha="1" type="marker" name="@23@0">
            <layer pass="0" class="SvgMarker" locked="0">
              <prop k="angle" v="0"/>
              <prop k="fill" v="#828282"/>
              <prop k="horizontal_anchor_point" v="1"/>
              <prop k="name" v="/grundbuchplan/symbol_c_schilfguertel_param.svg"/>
              <prop k="offset" v="0,0"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="outline" v="#000000"/>
              <prop k="outline-width" v="1"/>
              <prop k="outline_width_unit" v="MM"/>
              <prop k="size" v="4.2"/>
              <prop k="size_unit" v="MM"/>
              <prop k="vertical_anchor_point" v="1"/>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol alpha="1" type="fill" name="24">
        <layer pass="0" class="PointPatternFill" locked="0">
          <prop k="displacement_x" v="7"/>
          <prop k="displacement_x_unit" v="MM"/>
          <prop k="displacement_y" v="0"/>
          <prop k="displacement_y_unit" v="MM"/>
          <prop k="distance_x" v="14"/>
          <prop k="distance_x_unit" v="MM"/>
          <prop k="distance_y" v="14"/>
          <prop k="distance_y_unit" v="MM"/>
          <symbol alpha="1" type="marker" name="@24@0">
            <layer pass="0" class="SvgMarker" locked="0">
              <prop k="angle" v="0"/>
              <prop k="fill" v="#828282"/>
              <prop k="horizontal_anchor_point" v="1"/>
              <prop k="name" v="/grundbuchplan/symbol_c_schilfguertel_param.svg"/>
              <prop k="offset" v="0,0"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="outline" v="#000000"/>
              <prop k="outline-width" v="1"/>
              <prop k="outline_width_unit" v="MM"/>
              <prop k="size" v="4.2"/>
              <prop k="size_unit" v="MM"/>
              <prop k="vertical_anchor_point" v="1"/>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol alpha="1" type="fill" name="25">
        <layer pass="0" class="PointPatternFill" locked="0">
          <prop k="displacement_x" v="5"/>
          <prop k="displacement_x_unit" v="MM"/>
          <prop k="displacement_y" v="0"/>
          <prop k="displacement_y_unit" v="MM"/>
          <prop k="distance_x" v="10"/>
          <prop k="distance_x_unit" v="MM"/>
          <prop k="distance_y" v="10"/>
          <prop k="distance_y_unit" v="MM"/>
          <symbol alpha="1" type="marker" name="@25@0">
            <layer pass="0" class="SvgMarker" locked="0">
              <prop k="angle" v="0"/>
              <prop k="fill" v="#828282"/>
              <prop k="horizontal_anchor_point" v="1"/>
              <prop k="name" v="/grundbuchplan/symbol_c_schilfguertel_param.svg"/>
              <prop k="offset" v="0,0"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="outline" v="#000000"/>
              <prop k="outline-width" v="1"/>
              <prop k="outline_width_unit" v="MM"/>
              <prop k="size" v="3"/>
              <prop k="size_unit" v="MM"/>
              <prop k="vertical_anchor_point" v="1"/>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol alpha="1" type="fill" name="26">
        <layer pass="0" class="PointPatternFill" locked="0">
          <prop k="displacement_x" v="3.5"/>
          <prop k="displacement_x_unit" v="MM"/>
          <prop k="displacement_y" v="0"/>
          <prop k="displacement_y_unit" v="MM"/>
          <prop k="distance_x" v="7"/>
          <prop k="distance_x_unit" v="MM"/>
          <prop k="distance_y" v="7"/>
          <prop k="distance_y_unit" v="MM"/>
          <symbol alpha="1" type="marker" name="@26@0">
            <layer pass="0" class="SvgMarker" locked="0">
              <prop k="angle" v="0"/>
              <prop k="fill" v="#828282"/>
              <prop k="horizontal_anchor_point" v="1"/>
              <prop k="name" v="/grundbuchplan/symbol_c_schilfguertel_param.svg"/>
              <prop k="offset" v="0,0"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="outline" v="#000000"/>
              <prop k="outline-width" v="1"/>
              <prop k="outline_width_unit" v="MM"/>
              <prop k="size" v="2.1"/>
              <prop k="size_unit" v="MM"/>
              <prop k="vertical_anchor_point" v="1"/>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol alpha="1" type="fill" name="27">
        <layer pass="0" class="PointPatternFill" locked="0">
          <prop k="displacement_x" v="2.45"/>
          <prop k="displacement_x_unit" v="MM"/>
          <prop k="displacement_y" v="0"/>
          <prop k="displacement_y_unit" v="MM"/>
          <prop k="distance_x" v="4.9"/>
          <prop k="distance_x_unit" v="MM"/>
          <prop k="distance_y" v="4.9"/>
          <prop k="distance_y_unit" v="MM"/>
          <symbol alpha="1" type="marker" name="@27@0">
            <layer pass="0" class="SvgMarker" locked="0">
              <prop k="angle" v="0"/>
              <prop k="fill" v="#828282"/>
              <prop k="horizontal_anchor_point" v="1"/>
              <prop k="name" v="/grundbuchplan/symbol_c_schilfguertel_param.svg"/>
              <prop k="offset" v="0,0"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="outline" v="#000000"/>
              <prop k="outline-width" v="1"/>
              <prop k="outline_width_unit" v="MM"/>
              <prop k="size" v="1.5"/>
              <prop k="size_unit" v="MM"/>
              <prop k="vertical_anchor_point" v="1"/>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol alpha="1" type="fill" name="28">
        <layer pass="0" class="PointPatternFill" locked="0">
          <prop k="displacement_x" v="1.4"/>
          <prop k="displacement_x_unit" v="MM"/>
          <prop k="displacement_y" v="0"/>
          <prop k="displacement_y_unit" v="MM"/>
          <prop k="distance_x" v="2.8"/>
          <prop k="distance_x_unit" v="MM"/>
          <prop k="distance_y" v="2.8"/>
          <prop k="distance_y_unit" v="MM"/>
          <symbol alpha="1" type="marker" name="@28@0">
            <layer pass="0" class="SimpleMarker" locked="0">
              <prop k="angle" v="0"/>
              <prop k="color" v="0,0,0,255"/>
              <prop k="color_border" v="0,0,0,0"/>
              <prop k="horizontal_anchor_point" v="1"/>
              <prop k="name" v="circle"/>
              <prop k="offset" v="0,0"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="outline_width" v="0"/>
              <prop k="outline_width_unit" v="MM"/>
              <prop k="scale_method" v="area"/>
              <prop k="size" v="0.42"/>
              <prop k="size_unit" v="MM"/>
              <prop k="vertical_anchor_point" v="1"/>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol alpha="1" type="fill" name="29">
        <layer pass="0" class="PointPatternFill" locked="0">
          <prop k="displacement_x" v="1.4"/>
          <prop k="displacement_x_unit" v="MM"/>
          <prop k="displacement_y" v="0"/>
          <prop k="displacement_y_unit" v="MM"/>
          <prop k="distance_x" v="2.8"/>
          <prop k="distance_x_unit" v="MM"/>
          <prop k="distance_y" v="2.8"/>
          <prop k="distance_y_unit" v="MM"/>
          <symbol alpha="1" type="marker" name="@29@0">
            <layer pass="0" class="SimpleMarker" locked="0">
              <prop k="angle" v="0"/>
              <prop k="color" v="0,0,0,255"/>
              <prop k="color_border" v="0,0,0,0"/>
              <prop k="horizontal_anchor_point" v="1"/>
              <prop k="name" v="circle"/>
              <prop k="offset" v="0,0"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="outline_width" v="0"/>
              <prop k="outline_width_unit" v="MM"/>
              <prop k="scale_method" v="area"/>
              <prop k="size" v="0.42"/>
              <prop k="size_unit" v="MM"/>
              <prop k="vertical_anchor_point" v="1"/>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol alpha="1" type="fill" name="3">
        <layer pass="90" class="SimpleLine" locked="0">
          <prop k="capstyle" v="square"/>
          <prop k="color" v="255,255,255,255"/>
          <prop k="customdash" v="5;2"/>
          <prop k="customdash_unit" v="MM"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="penstyle" v="solid"/>
          <prop k="use_custom_dash" v="0"/>
          <prop k="width" v="0.2"/>
          <prop k="width_unit" v="MM"/>
        </layer>
        <layer pass="90" class="SimpleLine" locked="0">
          <prop k="capstyle" v="flat"/>
          <prop k="color" v="0,0,0,255"/>
          <prop k="customdash" v="1.05;0.35"/>
          <prop k="customdash_unit" v="MM"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="penstyle" v="solid"/>
          <prop k="use_custom_dash" v="1"/>
          <prop k="width" v="0.14"/>
          <prop k="width_unit" v="MM"/>
        </layer>
      </symbol>
      <symbol alpha="1" type="fill" name="30">
        <layer pass="0" class="PointPatternFill" locked="0">
          <prop k="displacement_x" v="1"/>
          <prop k="displacement_x_unit" v="MM"/>
          <prop k="displacement_y" v="0"/>
          <prop k="displacement_y_unit" v="MM"/>
          <prop k="distance_x" v="2"/>
          <prop k="distance_x_unit" v="MM"/>
          <prop k="distance_y" v="2"/>
          <prop k="distance_y_unit" v="MM"/>
          <symbol alpha="1" type="marker" name="@30@0">
            <layer pass="0" class="SimpleMarker" locked="0">
              <prop k="angle" v="0"/>
              <prop k="color" v="0,0,0,255"/>
              <prop k="color_border" v="0,0,0,0"/>
              <prop k="horizontal_anchor_point" v="1"/>
              <prop k="name" v="circle"/>
              <prop k="offset" v="0,0"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="outline_width" v="0"/>
              <prop k="outline_width_unit" v="MM"/>
              <prop k="scale_method" v="area"/>
              <prop k="size" v="0.3"/>
              <prop k="size_unit" v="MM"/>
              <prop k="vertical_anchor_point" v="1"/>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol alpha="1" type="fill" name="31">
        <layer pass="0" class="PointPatternFill" locked="0">
          <prop k="displacement_x" v="0.7"/>
          <prop k="displacement_x_unit" v="MM"/>
          <prop k="displacement_y" v="0"/>
          <prop k="displacement_y_unit" v="MM"/>
          <prop k="distance_x" v="1.4"/>
          <prop k="distance_x_unit" v="MM"/>
          <prop k="distance_y" v="1.4"/>
          <prop k="distance_y_unit" v="MM"/>
          <symbol alpha="1" type="marker" name="@31@0">
            <layer pass="0" class="SimpleMarker" locked="0">
              <prop k="angle" v="0"/>
              <prop k="color" v="0,0,0,255"/>
              <prop k="color_border" v="0,0,0,0"/>
              <prop k="horizontal_anchor_point" v="1"/>
              <prop k="name" v="circle"/>
              <prop k="offset" v="0,0"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="outline_width" v="0"/>
              <prop k="outline_width_unit" v="MM"/>
              <prop k="scale_method" v="area"/>
              <prop k="size" v="0.21"/>
              <prop k="size_unit" v="MM"/>
              <prop k="vertical_anchor_point" v="1"/>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol alpha="1" type="fill" name="32">
        <layer pass="0" class="PointPatternFill" locked="0">
          <prop k="displacement_x" v="0.5"/>
          <prop k="displacement_x_unit" v="MM"/>
          <prop k="displacement_y" v="0"/>
          <prop k="displacement_y_unit" v="MM"/>
          <prop k="distance_x" v="1"/>
          <prop k="distance_x_unit" v="MM"/>
          <prop k="distance_y" v="1"/>
          <prop k="distance_y_unit" v="MM"/>
          <symbol alpha="1" type="marker" name="@32@0">
            <layer pass="0" class="SimpleMarker" locked="0">
              <prop k="angle" v="0"/>
              <prop k="color" v="0,0,0,255"/>
              <prop k="color_border" v="0,0,0,0"/>
              <prop k="horizontal_anchor_point" v="1"/>
              <prop k="name" v="circle"/>
              <prop k="offset" v="0,0"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="outline_width" v="0"/>
              <prop k="outline_width_unit" v="MM"/>
              <prop k="scale_method" v="area"/>
              <prop k="size" v="0.15"/>
              <prop k="size_unit" v="MM"/>
              <prop k="vertical_anchor_point" v="1"/>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol alpha="1" type="fill" name="33">
        <layer pass="0" class="PointPatternFill" locked="0">
          <prop k="displacement_x" v="2.8"/>
          <prop k="displacement_x_unit" v="MM"/>
          <prop k="displacement_y" v="0"/>
          <prop k="displacement_y_unit" v="MM"/>
          <prop k="distance_x" v="5.6"/>
          <prop k="distance_x_unit" v="MM"/>
          <prop k="distance_y" v="5.6"/>
          <prop k="distance_y_unit" v="MM"/>
          <symbol alpha="1" type="marker" name="@33@0">
            <layer pass="0" class="SimpleMarker" locked="0">
              <prop k="angle" v="0"/>
              <prop k="color" v="0,0,0,255"/>
              <prop k="color_border" v="0,0,0,0"/>
              <prop k="horizontal_anchor_point" v="1"/>
              <prop k="name" v="circle"/>
              <prop k="offset" v="0,0"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="outline_width" v="0"/>
              <prop k="outline_width_unit" v="MM"/>
              <prop k="scale_method" v="area"/>
              <prop k="size" v="0.42"/>
              <prop k="size_unit" v="MM"/>
              <prop k="vertical_anchor_point" v="1"/>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol alpha="1" type="fill" name="34">
        <layer pass="0" class="PointPatternFill" locked="0">
          <prop k="displacement_x" v="2.8"/>
          <prop k="displacement_x_unit" v="MM"/>
          <prop k="displacement_y" v="0"/>
          <prop k="displacement_y_unit" v="MM"/>
          <prop k="distance_x" v="5.6"/>
          <prop k="distance_x_unit" v="MM"/>
          <prop k="distance_y" v="5.6"/>
          <prop k="distance_y_unit" v="MM"/>
          <symbol alpha="1" type="marker" name="@34@0">
            <layer pass="0" class="SimpleMarker" locked="0">
              <prop k="angle" v="0"/>
              <prop k="color" v="0,0,0,255"/>
              <prop k="color_border" v="0,0,0,0"/>
              <prop k="horizontal_anchor_point" v="1"/>
              <prop k="name" v="circle"/>
              <prop k="offset" v="0,0"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="outline_width" v="0"/>
              <prop k="outline_width_unit" v="MM"/>
              <prop k="scale_method" v="area"/>
              <prop k="size" v="0.42"/>
              <prop k="size_unit" v="MM"/>
              <prop k="vertical_anchor_point" v="1"/>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol alpha="1" type="fill" name="35">
        <layer pass="0" class="PointPatternFill" locked="0">
          <prop k="displacement_x" v="2"/>
          <prop k="displacement_x_unit" v="MM"/>
          <prop k="displacement_y" v="0"/>
          <prop k="displacement_y_unit" v="MM"/>
          <prop k="distance_x" v="4"/>
          <prop k="distance_x_unit" v="MM"/>
          <prop k="distance_y" v="4"/>
          <prop k="distance_y_unit" v="MM"/>
          <symbol alpha="1" type="marker" name="@35@0">
            <layer pass="0" class="SimpleMarker" locked="0">
              <prop k="angle" v="0"/>
              <prop k="color" v="0,0,0,255"/>
              <prop k="color_border" v="0,0,0,0"/>
              <prop k="horizontal_anchor_point" v="1"/>
              <prop k="name" v="circle"/>
              <prop k="offset" v="0,0"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="outline_width" v="0"/>
              <prop k="outline_width_unit" v="MM"/>
              <prop k="scale_method" v="area"/>
              <prop k="size" v="0.3"/>
              <prop k="size_unit" v="MM"/>
              <prop k="vertical_anchor_point" v="1"/>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol alpha="1" type="fill" name="36">
        <layer pass="0" class="PointPatternFill" locked="0">
          <prop k="displacement_x" v="1.4"/>
          <prop k="displacement_x_unit" v="MM"/>
          <prop k="displacement_y" v="0"/>
          <prop k="displacement_y_unit" v="MM"/>
          <prop k="distance_x" v="2.8"/>
          <prop k="distance_x_unit" v="MM"/>
          <prop k="distance_y" v="2.8"/>
          <prop k="distance_y_unit" v="MM"/>
          <symbol alpha="1" type="marker" name="@36@0">
            <layer pass="0" class="SimpleMarker" locked="0">
              <prop k="angle" v="0"/>
              <prop k="color" v="0,0,0,255"/>
              <prop k="color_border" v="0,0,0,0"/>
              <prop k="horizontal_anchor_point" v="1"/>
              <prop k="name" v="circle"/>
              <prop k="offset" v="0,0"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="outline_width" v="0"/>
              <prop k="outline_width_unit" v="MM"/>
              <prop k="scale_method" v="area"/>
              <prop k="size" v="0.21"/>
              <prop k="size_unit" v="MM"/>
              <prop k="vertical_anchor_point" v="1"/>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol alpha="1" type="fill" name="37">
        <layer pass="0" class="PointPatternFill" locked="0">
          <prop k="displacement_x" v="1"/>
          <prop k="displacement_x_unit" v="MM"/>
          <prop k="displacement_y" v="0"/>
          <prop k="displacement_y_unit" v="MM"/>
          <prop k="distance_x" v="2"/>
          <prop k="distance_x_unit" v="MM"/>
          <prop k="distance_y" v="2"/>
          <prop k="distance_y_unit" v="MM"/>
          <symbol alpha="1" type="marker" name="@37@0">
            <layer pass="0" class="SimpleMarker" locked="0">
              <prop k="angle" v="0"/>
              <prop k="color" v="0,0,0,255"/>
              <prop k="color_border" v="0,0,0,0"/>
              <prop k="horizontal_anchor_point" v="1"/>
              <prop k="name" v="circle"/>
              <prop k="offset" v="0,0"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="outline_width" v="0"/>
              <prop k="outline_width_unit" v="MM"/>
              <prop k="scale_method" v="area"/>
              <prop k="size" v="0.21"/>
              <prop k="size_unit" v="MM"/>
              <prop k="vertical_anchor_point" v="1"/>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol alpha="1" type="fill" name="38">
        <layer pass="0" class="SVGFill" locked="0">
          <prop k="angle" v="0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="pattern_width_unit" v="MM"/>
          <prop k="svgFile" v="/grundbuchplan/symbol_1_fels_geroell_param.svg"/>
          <prop k="svgFillColor" v="#828282"/>
          <prop k="svgOutlineColor" v="#000000"/>
          <prop k="svgOutlineWidth" v="0.3"/>
          <prop k="svgOutlineWidth_expression" v="svgOutlineWidth_expression"/>
          <prop k="svg_outline_width_unit" v="MM"/>
          <prop k="width" v="4.2"/>
          <symbol alpha="1" type="line" name="@38@0">
            <layer pass="0" class="SimpleLine" locked="0">
              <prop k="capstyle" v="square"/>
              <prop k="color" v="0,0,0,255"/>
              <prop k="customdash" v="5;2"/>
              <prop k="customdash_unit" v="MM"/>
              <prop k="joinstyle" v="bevel"/>
              <prop k="offset" v="0"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="penstyle" v="no"/>
              <prop k="use_custom_dash" v="0"/>
              <prop k="width" v="0.26"/>
              <prop k="width_unit" v="MM"/>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol alpha="1" type="fill" name="39">
        <layer pass="0" class="SVGFill" locked="0">
          <prop k="angle" v="0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="pattern_width_unit" v="MM"/>
          <prop k="svgFile" v="/grundbuchplan/symbol_1_fels_geroell_param.svg"/>
          <prop k="svgFillColor" v="#828282"/>
          <prop k="svgOutlineColor" v="#000000"/>
          <prop k="svgOutlineWidth" v="0.3"/>
          <prop k="svgOutlineWidth_expression" v="svgOutlineWidth_expression"/>
          <prop k="svg_outline_width_unit" v="MM"/>
          <prop k="width" v="4.2"/>
          <symbol alpha="1" type="line" name="@39@0">
            <layer pass="0" class="SimpleLine" locked="0">
              <prop k="capstyle" v="square"/>
              <prop k="color" v="0,0,0,255"/>
              <prop k="customdash" v="5;2"/>
              <prop k="customdash_unit" v="MM"/>
              <prop k="joinstyle" v="bevel"/>
              <prop k="offset" v="0"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="penstyle" v="no"/>
              <prop k="use_custom_dash" v="0"/>
              <prop k="width" v="0.26"/>
              <prop k="width_unit" v="MM"/>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol alpha="1" type="fill" name="4">
        <layer pass="90" class="SimpleLine" locked="0">
          <prop k="capstyle" v="square"/>
          <prop k="color" v="255,255,255,255"/>
          <prop k="customdash" v="5;2"/>
          <prop k="customdash_unit" v="MM"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="penstyle" v="solid"/>
          <prop k="use_custom_dash" v="0"/>
          <prop k="width" v="0.15"/>
          <prop k="width_unit" v="MM"/>
        </layer>
        <layer pass="90" class="SimpleLine" locked="0">
          <prop k="capstyle" v="flat"/>
          <prop k="color" v="0,0,0,255"/>
          <prop k="customdash" v="0.73;0.24"/>
          <prop k="customdash_unit" v="MM"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="penstyle" v="solid"/>
          <prop k="use_custom_dash" v="1"/>
          <prop k="width" v="0.1"/>
          <prop k="width_unit" v="MM"/>
        </layer>
      </symbol>
      <symbol alpha="1" type="fill" name="40">
        <layer pass="0" class="SVGFill" locked="0">
          <prop k="angle" v="0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="pattern_width_unit" v="MM"/>
          <prop k="svgFile" v="/grundbuchplan/symbol_1_fels_geroell_param.svg"/>
          <prop k="svgFillColor" v="#828282"/>
          <prop k="svgOutlineColor" v="#000000"/>
          <prop k="svgOutlineWidth" v="0.3"/>
          <prop k="svgOutlineWidth_expression" v="svgOutlineWidth_expression"/>
          <prop k="svg_outline_width_unit" v="MM"/>
          <prop k="width" v="3"/>
          <symbol alpha="1" type="line" name="@40@0">
            <layer pass="0" class="SimpleLine" locked="0">
              <prop k="capstyle" v="square"/>
              <prop k="color" v="0,0,0,255"/>
              <prop k="customdash" v="5;2"/>
              <prop k="customdash_unit" v="MM"/>
              <prop k="joinstyle" v="bevel"/>
              <prop k="offset" v="0"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="penstyle" v="no"/>
              <prop k="use_custom_dash" v="0"/>
              <prop k="width" v="0.26"/>
              <prop k="width_unit" v="MM"/>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol alpha="1" type="fill" name="41">
        <layer pass="0" class="SVGFill" locked="0">
          <prop k="angle" v="0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="pattern_width_unit" v="MM"/>
          <prop k="svgFile" v="/grundbuchplan/symbol_1_fels_geroell_param.svg"/>
          <prop k="svgFillColor" v="#828282"/>
          <prop k="svgOutlineColor" v="#000000"/>
          <prop k="svgOutlineWidth" v="0.3"/>
          <prop k="svgOutlineWidth_expression" v="svgOutlineWidth_expression"/>
          <prop k="svg_outline_width_unit" v="MM"/>
          <prop k="width" v="2.1"/>
          <symbol alpha="1" type="line" name="@41@0">
            <layer pass="0" class="SimpleLine" locked="0">
              <prop k="capstyle" v="square"/>
              <prop k="color" v="0,0,0,255"/>
              <prop k="customdash" v="5;2"/>
              <prop k="customdash_unit" v="MM"/>
              <prop k="joinstyle" v="bevel"/>
              <prop k="offset" v="0"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="penstyle" v="no"/>
              <prop k="use_custom_dash" v="0"/>
              <prop k="width" v="0.26"/>
              <prop k="width_unit" v="MM"/>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol alpha="1" type="fill" name="42">
        <layer pass="0" class="SVGFill" locked="0">
          <prop k="angle" v="0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="pattern_width_unit" v="MM"/>
          <prop k="svgFile" v="/grundbuchplan/symbol_1_fels_geroell_param.svg"/>
          <prop k="svgFillColor" v="#000000"/>
          <prop k="svgOutlineColor" v="#000000"/>
          <prop k="svgOutlineWidth" v="0.3"/>
          <prop k="svgOutlineWidth_expression" v="svgOutlineWidth_expression"/>
          <prop k="svg_outline_width_unit" v="MM"/>
          <prop k="width" v="1.5"/>
          <symbol alpha="1" type="line" name="@42@0">
            <layer pass="0" class="SimpleLine" locked="0">
              <prop k="capstyle" v="square"/>
              <prop k="color" v="0,0,0,255"/>
              <prop k="customdash" v="5;2"/>
              <prop k="customdash_unit" v="MM"/>
              <prop k="joinstyle" v="bevel"/>
              <prop k="offset" v="0"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="penstyle" v="no"/>
              <prop k="use_custom_dash" v="0"/>
              <prop k="width" v="0.26"/>
              <prop k="width_unit" v="MM"/>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol alpha="1" type="fill" name="43">
        <layer pass="0" class="SVGFill" locked="0">
          <prop k="angle" v="0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="pattern_width_unit" v="MM"/>
          <prop k="svgFile" v="/grundbuchplan/symbol_2_geroell_param.svg"/>
          <prop k="svgFillColor" v="#828282"/>
          <prop k="svgOutlineColor" v="#000000"/>
          <prop k="svgOutlineWidth" v="0.3"/>
          <prop k="svgOutlineWidth_expression" v="svgOutlineWidth_expression"/>
          <prop k="svg_outline_width_unit" v="MM"/>
          <prop k="width" v="2.8"/>
          <symbol alpha="1" type="line" name="@43@0">
            <layer pass="0" class="SimpleLine" locked="0">
              <prop k="capstyle" v="square"/>
              <prop k="color" v="0,0,0,255"/>
              <prop k="customdash" v="5;2"/>
              <prop k="customdash_unit" v="MM"/>
              <prop k="joinstyle" v="bevel"/>
              <prop k="offset" v="0"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="penstyle" v="no"/>
              <prop k="use_custom_dash" v="0"/>
              <prop k="width" v="0.26"/>
              <prop k="width_unit" v="MM"/>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol alpha="1" type="fill" name="44">
        <layer pass="0" class="SVGFill" locked="0">
          <prop k="angle" v="0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="pattern_width_unit" v="MM"/>
          <prop k="svgFile" v="/grundbuchplan/symbol_2_geroell_param.svg"/>
          <prop k="svgFillColor" v="#828282"/>
          <prop k="svgOutlineColor" v="#000000"/>
          <prop k="svgOutlineWidth" v="0.3"/>
          <prop k="svgOutlineWidth_expression" v="svgOutlineWidth_expression"/>
          <prop k="svg_outline_width_unit" v="MM"/>
          <prop k="width" v="2.8"/>
          <symbol alpha="1" type="line" name="@44@0">
            <layer pass="0" class="SimpleLine" locked="0">
              <prop k="capstyle" v="square"/>
              <prop k="color" v="0,0,0,255"/>
              <prop k="customdash" v="5;2"/>
              <prop k="customdash_unit" v="MM"/>
              <prop k="joinstyle" v="bevel"/>
              <prop k="offset" v="0"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="penstyle" v="no"/>
              <prop k="use_custom_dash" v="0"/>
              <prop k="width" v="0.26"/>
              <prop k="width_unit" v="MM"/>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol alpha="1" type="fill" name="45">
        <layer pass="0" class="SVGFill" locked="0">
          <prop k="angle" v="0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="pattern_width_unit" v="MM"/>
          <prop k="svgFile" v="/grundbuchplan/symbol_2_geroell_param.svg"/>
          <prop k="svgFillColor" v="#828282"/>
          <prop k="svgOutlineColor" v="#000000"/>
          <prop k="svgOutlineWidth" v="0.3"/>
          <prop k="svgOutlineWidth_expression" v="svgOutlineWidth_expression"/>
          <prop k="svg_outline_width_unit" v="MM"/>
          <prop k="width" v="2"/>
          <symbol alpha="1" type="line" name="@45@0">
            <layer pass="0" class="SimpleLine" locked="0">
              <prop k="capstyle" v="square"/>
              <prop k="color" v="0,0,0,255"/>
              <prop k="customdash" v="5;2"/>
              <prop k="customdash_unit" v="MM"/>
              <prop k="joinstyle" v="bevel"/>
              <prop k="offset" v="0"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="penstyle" v="no"/>
              <prop k="use_custom_dash" v="0"/>
              <prop k="width" v="0.26"/>
              <prop k="width_unit" v="MM"/>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol alpha="1" type="fill" name="46">
        <layer pass="0" class="SVGFill" locked="0">
          <prop k="angle" v="0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="pattern_width_unit" v="MM"/>
          <prop k="svgFile" v="/grundbuchplan/symbol_2_geroell_param.svg"/>
          <prop k="svgFillColor" v="#828282"/>
          <prop k="svgOutlineColor" v="#000000"/>
          <prop k="svgOutlineWidth" v="0.3"/>
          <prop k="svgOutlineWidth_expression" v="svgOutlineWidth_expression"/>
          <prop k="svg_outline_width_unit" v="MM"/>
          <prop k="width" v="1.4"/>
          <symbol alpha="1" type="line" name="@46@0">
            <layer pass="0" class="SimpleLine" locked="0">
              <prop k="capstyle" v="square"/>
              <prop k="color" v="0,0,0,255"/>
              <prop k="customdash" v="5;2"/>
              <prop k="customdash_unit" v="MM"/>
              <prop k="joinstyle" v="bevel"/>
              <prop k="offset" v="0"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="penstyle" v="no"/>
              <prop k="use_custom_dash" v="0"/>
              <prop k="width" v="0.26"/>
              <prop k="width_unit" v="MM"/>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol alpha="1" type="fill" name="47">
        <layer pass="0" class="SVGFill" locked="0">
          <prop k="angle" v="0"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="pattern_width_unit" v="MM"/>
          <prop k="svgFile" v="/grundbuchplan/symbol_1_fels_geroell_param.svg"/>
          <prop k="svgFillColor" v="#000000"/>
          <prop k="svgOutlineColor" v="#000000"/>
          <prop k="svgOutlineWidth" v="0.3"/>
          <prop k="svgOutlineWidth_expression" v="svgOutlineWidth_expression"/>
          <prop k="svg_outline_width_unit" v="MM"/>
          <prop k="width" v="1.5"/>
          <symbol alpha="1" type="line" name="@47@0">
            <layer pass="0" class="SimpleLine" locked="0">
              <prop k="capstyle" v="square"/>
              <prop k="color" v="0,0,0,255"/>
              <prop k="customdash" v="5;2"/>
              <prop k="customdash_unit" v="MM"/>
              <prop k="joinstyle" v="bevel"/>
              <prop k="offset" v="0"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="penstyle" v="no"/>
              <prop k="use_custom_dash" v="0"/>
              <prop k="width" v="0.26"/>
              <prop k="width_unit" v="MM"/>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol alpha="1" type="fill" name="5">
        <layer pass="90" class="SimpleLine" locked="0">
          <prop k="capstyle" v="square"/>
          <prop k="color" v="255,255,255,255"/>
          <prop k="customdash" v="5;2"/>
          <prop k="customdash_unit" v="MM"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="penstyle" v="solid"/>
          <prop k="use_custom_dash" v="0"/>
          <prop k="width" v="0.15"/>
          <prop k="width_unit" v="MM"/>
        </layer>
        <layer pass="90" class="SimpleLine" locked="0">
          <prop k="capstyle" v="flat"/>
          <prop k="color" v="0,0,0,255"/>
          <prop k="customdash" v="1.5;0.5"/>
          <prop k="customdash_unit" v="MM"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="penstyle" v="solid"/>
          <prop k="use_custom_dash" v="0"/>
          <prop k="width" v="0.1"/>
          <prop k="width_unit" v="MM"/>
        </layer>
      </symbol>
      <symbol alpha="1" type="fill" name="6">
        <layer pass="99" class="SimpleLine" locked="0">
          <prop k="capstyle" v="square"/>
          <prop k="color" v="255,255,255,255"/>
          <prop k="customdash" v="5;2"/>
          <prop k="customdash_unit" v="MM"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="penstyle" v="solid"/>
          <prop k="use_custom_dash" v="0"/>
          <prop k="width" v="0.35"/>
          <prop k="width_unit" v="MM"/>
        </layer>
        <layer pass="99" class="SimpleLine" locked="0">
          <prop k="capstyle" v="flat"/>
          <prop k="color" v="0,0,0,255"/>
          <prop k="customdash" v="1.5;0.5"/>
          <prop k="customdash_unit" v="MM"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="penstyle" v="solid"/>
          <prop k="use_custom_dash" v="0"/>
          <prop k="width" v="0.28"/>
          <prop k="width_unit" v="MM"/>
        </layer>
      </symbol>
      <symbol alpha="1" type="fill" name="7">
        <layer pass="99" class="SimpleLine" locked="0">
          <prop k="capstyle" v="square"/>
          <prop k="color" v="255,255,255,255"/>
          <prop k="customdash" v="5;2"/>
          <prop k="customdash_unit" v="MM"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="penstyle" v="solid"/>
          <prop k="use_custom_dash" v="0"/>
          <prop k="width" v="0.35"/>
          <prop k="width_unit" v="MM"/>
        </layer>
        <layer pass="99" class="SimpleLine" locked="0">
          <prop k="capstyle" v="flat"/>
          <prop k="color" v="0,0,0,255"/>
          <prop k="customdash" v="1.5;0.5"/>
          <prop k="customdash_unit" v="MM"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="penstyle" v="solid"/>
          <prop k="use_custom_dash" v="0"/>
          <prop k="width" v="0.28"/>
          <prop k="width_unit" v="MM"/>
        </layer>
      </symbol>
      <symbol alpha="1" type="fill" name="8">
        <layer pass="99" class="SimpleLine" locked="0">
          <prop k="capstyle" v="square"/>
          <prop k="color" v="255,255,255,255"/>
          <prop k="customdash" v="5;2"/>
          <prop k="customdash_unit" v="MM"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="penstyle" v="solid"/>
          <prop k="use_custom_dash" v="0"/>
          <prop k="width" v="0.2"/>
          <prop k="width_unit" v="MM"/>
        </layer>
        <layer pass="99" class="SimpleLine" locked="0">
          <prop k="capstyle" v="flat"/>
          <prop k="color" v="0,0,0,255"/>
          <prop k="customdash" v="1.5;0.5"/>
          <prop k="customdash_unit" v="MM"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="penstyle" v="solid"/>
          <prop k="use_custom_dash" v="0"/>
          <prop k="width" v="0.2"/>
          <prop k="width_unit" v="MM"/>
        </layer>
      </symbol>
      <symbol alpha="1" type="fill" name="9">
        <layer pass="99" class="SimpleLine" locked="0">
          <prop k="capstyle" v="square"/>
          <prop k="color" v="255,255,255,255"/>
          <prop k="customdash" v="5;2"/>
          <prop k="customdash_unit" v="MM"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="penstyle" v="solid"/>
          <prop k="use_custom_dash" v="0"/>
          <prop k="width" v="0.14"/>
          <prop k="width_unit" v="MM"/>
        </layer>
        <layer pass="99" class="SimpleLine" locked="0">
          <prop k="capstyle" v="flat"/>
          <prop k="color" v="0,0,0,255"/>
          <prop k="customdash" v="1.5;0.5"/>
          <prop k="customdash_unit" v="MM"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="penstyle" v="solid"/>
          <prop k="use_custom_dash" v="0"/>
          <prop k="width" v="0.14"/>
          <prop k="width_unit" v="MM"/>
        </layer>
      </symbol>
    </symbols>
  </renderer-v2>
  <customproperties>
    <property key="labeling" value="pal"/>
    <property key="labeling/addDirectionSymbol" value="false"/>
    <property key="labeling/angleOffset" value="0"/>
    <property key="labeling/blendMode" value="0"/>
    <property key="labeling/bufferBlendMode" value="0"/>
    <property key="labeling/bufferColorA" value="255"/>
    <property key="labeling/bufferColorB" value="255"/>
    <property key="labeling/bufferColorG" value="255"/>
    <property key="labeling/bufferColorR" value="255"/>
    <property key="labeling/bufferDraw" value="true"/>
    <property key="labeling/bufferJoinStyle" value="64"/>
    <property key="labeling/bufferNoFill" value="false"/>
    <property key="labeling/bufferSize" value="1"/>
    <property key="labeling/bufferSizeInMapUnits" value="false"/>
    <property key="labeling/bufferTransp" value="0"/>
    <property key="labeling/centroidWhole" value="false"/>
    <property key="labeling/decimals" value="0"/>
    <property key="labeling/displayAll" value="false"/>
    <property key="labeling/dist" value="0"/>
    <property key="labeling/distInMapUnits" value="false"/>
    <property key="labeling/enabled" value="false"/>
    <property key="labeling/fieldName" value=""/>
    <property key="labeling/fontBold" value="true"/>
    <property key="labeling/fontCapitals" value="0"/>
    <property key="labeling/fontFamily" value="Ubuntu"/>
    <property key="labeling/fontItalic" value="true"/>
    <property key="labeling/fontLetterSpacing" value="0"/>
    <property key="labeling/fontLimitPixelSize" value="false"/>
    <property key="labeling/fontMaxPixelSize" value="10000"/>
    <property key="labeling/fontMinPixelSize" value="3"/>
    <property key="labeling/fontSize" value="10"/>
    <property key="labeling/fontSizeInMapUnits" value="false"/>
    <property key="labeling/fontStrikeout" value="false"/>
    <property key="labeling/fontUnderline" value="false"/>
    <property key="labeling/fontWeight" value="75"/>
    <property key="labeling/fontWordSpacing" value="0"/>
    <property key="labeling/formatNumbers" value="false"/>
    <property key="labeling/isExpression" value="false"/>
    <property key="labeling/labelOffsetInMapUnits" value="true"/>
    <property key="labeling/labelPerPart" value="false"/>
    <property key="labeling/leftDirectionSymbol" value="&lt;"/>
    <property key="labeling/limitNumLabels" value="false"/>
    <property key="labeling/maxCurvedCharAngleIn" value="20"/>
    <property key="labeling/maxCurvedCharAngleOut" value="-20"/>
    <property key="labeling/maxNumLabels" value="2000"/>
    <property key="labeling/mergeLines" value="false"/>
    <property key="labeling/minFeatureSize" value="0"/>
    <property key="labeling/multilineAlign" value="0"/>
    <property key="labeling/multilineHeight" value="1"/>
    <property key="labeling/namedStyle" value="Bold Italic"/>
    <property key="labeling/obstacle" value="true"/>
    <property key="labeling/placeDirectionSymbol" value="0"/>
    <property key="labeling/placement" value="0"/>
    <property key="labeling/placementFlags" value="0"/>
    <property key="labeling/plussign" value="false"/>
    <property key="labeling/preserveRotation" value="true"/>
    <property key="labeling/previewBkgrdColor" value="#ffffff"/>
    <property key="labeling/priority" value="5"/>
    <property key="labeling/quadOffset" value="4"/>
    <property key="labeling/reverseDirectionSymbol" value="false"/>
    <property key="labeling/rightDirectionSymbol" value=">"/>
    <property key="labeling/scaleMax" value="10000000"/>
    <property key="labeling/scaleMin" value="1"/>
    <property key="labeling/scaleVisibility" value="false"/>
    <property key="labeling/shadowBlendMode" value="6"/>
    <property key="labeling/shadowColorB" value="0"/>
    <property key="labeling/shadowColorG" value="0"/>
    <property key="labeling/shadowColorR" value="0"/>
    <property key="labeling/shadowDraw" value="false"/>
    <property key="labeling/shadowOffsetAngle" value="135"/>
    <property key="labeling/shadowOffsetDist" value="1"/>
    <property key="labeling/shadowOffsetGlobal" value="true"/>
    <property key="labeling/shadowOffsetUnits" value="1"/>
    <property key="labeling/shadowRadius" value="1.5"/>
    <property key="labeling/shadowRadiusAlphaOnly" value="false"/>
    <property key="labeling/shadowRadiusUnits" value="1"/>
    <property key="labeling/shadowScale" value="100"/>
    <property key="labeling/shadowTransparency" value="30"/>
    <property key="labeling/shadowUnder" value="0"/>
    <property key="labeling/shapeBlendMode" value="0"/>
    <property key="labeling/shapeBorderColorA" value="255"/>
    <property key="labeling/shapeBorderColorB" value="128"/>
    <property key="labeling/shapeBorderColorG" value="128"/>
    <property key="labeling/shapeBorderColorR" value="128"/>
    <property key="labeling/shapeBorderWidth" value="0"/>
    <property key="labeling/shapeBorderWidthUnits" value="1"/>
    <property key="labeling/shapeDraw" value="false"/>
    <property key="labeling/shapeFillColorA" value="255"/>
    <property key="labeling/shapeFillColorB" value="255"/>
    <property key="labeling/shapeFillColorG" value="255"/>
    <property key="labeling/shapeFillColorR" value="255"/>
    <property key="labeling/shapeJoinStyle" value="64"/>
    <property key="labeling/shapeOffsetUnits" value="1"/>
    <property key="labeling/shapeOffsetX" value="0"/>
    <property key="labeling/shapeOffsetY" value="0"/>
    <property key="labeling/shapeRadiiUnits" value="1"/>
    <property key="labeling/shapeRadiiX" value="0"/>
    <property key="labeling/shapeRadiiY" value="0"/>
    <property key="labeling/shapeRotation" value="0"/>
    <property key="labeling/shapeRotationType" value="0"/>
    <property key="labeling/shapeSVGFile" value=""/>
    <property key="labeling/shapeSizeType" value="0"/>
    <property key="labeling/shapeSizeUnits" value="1"/>
    <property key="labeling/shapeSizeX" value="0"/>
    <property key="labeling/shapeSizeY" value="0"/>
    <property key="labeling/shapeTransparency" value="0"/>
    <property key="labeling/shapeType" value="0"/>
    <property key="labeling/textColorA" value="255"/>
    <property key="labeling/textColorB" value="0"/>
    <property key="labeling/textColorG" value="0"/>
    <property key="labeling/textColorR" value="0"/>
    <property key="labeling/textTransp" value="0"/>
    <property key="labeling/upsidedownLabels" value="0"/>
    <property key="labeling/wrapChar" value=""/>
    <property key="labeling/xOffset" value="0"/>
    <property key="labeling/xQuadOffset" value="0"/>
    <property key="labeling/yOffset" value="0"/>
    <property key="labeling/yQuadOffset" value="0"/>
  </customproperties>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerTransparency>0</layerTransparency>
  <displayfield>ogc_fid</displayfield>
  <label>0</label>
  <labelattributes>
    <label fieldname="" text="Label"/>
    <family fieldname="" name="Ubuntu"/>
    <size fieldname="" units="pt" value="12"/>
    <bold fieldname="" on="0"/>
    <italic fieldname="" on="0"/>
    <underline fieldname="" on="0"/>
    <strikeout fieldname="" on="0"/>
    <color fieldname="" red="0" blue="0" green="0"/>
    <x fieldname=""/>
    <y fieldname=""/>
    <offset x="0" y="0" units="pt" yfieldname="" xfieldname=""/>
    <angle fieldname="" value="0" auto="0"/>
    <alignment fieldname="" value="center"/>
    <buffercolor fieldname="" red="255" blue="255" green="255"/>
    <buffersize fieldname="" units="pt" value="1"/>
    <bufferenabled fieldname="" on=""/>
    <multilineenabled fieldname="" on=""/>
    <selectedonly on=""/>
  </labelattributes>
  <edittypes>
    <edittype labelontop="0" editable="1" type="0" name="art"/>
    <edittype labelontop="0" editable="1" type="0" name="art_txt"/>
    <edittype labelontop="0" editable="1" type="0" name="bfsnr"/>
    <edittype labelontop="0" editable="1" type="0" name="entstehung"/>
    <edittype labelontop="0" editable="1" type="0" name="gwr_egid"/>
    <edittype labelontop="0" editable="1" type="0" name="ogc_fid"/>
    <edittype labelontop="0" editable="1" type="0" name="qualitaet"/>
    <edittype labelontop="0" editable="1" type="0" name="qualitaet_txt"/>
    <edittype labelontop="0" editable="1" type="0" name="tid"/>
  </edittypes>
  <editform></editform>
  <editforminit></editforminit>
  <featformsuppress>0</featformsuppress>
  <annotationform>../Plan_fuer_das_Grundbuch</annotationform>
  <editorlayout>generatedlayout</editorlayout>
  <excludeAttributesWMS/>
  <excludeAttributesWFS/>
  <attributeactions/>
</qgis>
