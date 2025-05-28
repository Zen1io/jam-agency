document.addEventListener('DOMContentLoaded', function () {
  const serviceSelect = document.getElementById('service_type');
  const materialSelect = document.getElementById('material');

  const materialOptions = {
    billboard: ['banner_fabric', 'mesh', 'lightbox_film'],
    stand: ['pvc', 'plastic', 'composite'],
    showcase: ['vinyl', 'perforated_vinyl', 'uv_acrylic'],
    car_wrap: ['vinyl_gloss', 'vinyl_matte', 'vinyl_special'],
    facade_banner: ['reinforced_banner', 'mesh', 'blockout'],
    letters: ['acrylic', 'plastic', 'metal', 'composite_led'],
  };

  const allMaterials = {
    banner_fabric: 'Баннерная ткань',
    mesh: 'Сетка',
    lightbox_film: 'Лайтбокс-плёнка',
    pvc: 'ПВХ',
    plastic: 'Пластик',
    composite: 'Композит',
    vinyl: 'Виниловая плёнка',
    perforated_vinyl: 'Перфорированная плёнка',
    uv_acrylic: 'УФ печать на акриле',
    vinyl_gloss: 'Винил глянец',
    vinyl_matte: 'Винил матовый',
    vinyl_special: 'Винил спецэффект',
    reinforced_banner: 'Прочный баннер',
    blockout: 'Блок-аут',
    acrylic: 'Акрил',
    metal: 'Металл',
    composite_led: 'Композит с подсветкой',
  };

const selectedMaterial = "{{ selected_material|escapejs }}";

function updateMaterialOptions(service) {
  materialSelect.innerHTML = '';
  if (materialOptions[service]) {
    materialOptions[service].forEach(materialKey => {
      const option = document.createElement('option');
      option.value = materialKey;
      option.textContent = allMaterials[materialKey];
      if (materialKey === selectedMaterial) {
        option.selected = true;
      }
      materialSelect.appendChild(option);
    });
  }
}

  serviceSelect.addEventListener('change', function () {
    updateMaterialOptions(this.value);
  });

  updateMaterialOptions(serviceSelect.value); // init
});
