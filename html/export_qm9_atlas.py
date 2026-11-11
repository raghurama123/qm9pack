# python3.11 export_qm9_atlas.py --output qm9_atlas.json

#!/usr/bin/env python3
"""Export QM9PACK into a compact dataset for QM9 3D Inertia Navigator.
Usage: python export_qm9_atlas.py --output qm9_atlas.json
"""
import argparse, ast, json, math
import numpy as np
from qm9pack import get_data

MASS = {'H':1.00784,'C':12.011,'N':14.007,'O':15.999,'F':18.998403163}

def parse_atoms(v):
    if isinstance(v, str):
        try: v=ast.literal_eval(v)
        except (ValueError,SyntaxError):
            v=[x.strip().strip("'\" ") for x in v.strip('[]').split(',')]
    return [str(x).strip() for x in v]

def parse_coords(v):
    if isinstance(v, str):
        try: v=ast.literal_eval(v)
        except (ValueError,SyntaxError):
            v=[float(x) for x in v.replace('[',' ').replace(']',' ').replace(',',' ').split()]
    return np.asarray(v,dtype=float).reshape(-1,3)

def moments(atoms, xyz):
    masses=np.asarray([MASS[a] for a in atoms]); xyz=xyz-np.average(xyz,axis=0,weights=masses)
    tensor=np.sum(masses[:,None,None]*np.einsum('ni,nj->nij',xyz,xyz),axis=0)
    inertia=np.trace(tensor)*np.eye(3)-tensor
    return np.maximum(np.linalg.eigvalsh(inertia),0)

def run(output):
    df=get_data('qm9')
    result=[]; errors=[]
    for rowid, r in df.iterrows():
        try:
            atoms=parse_atoms(r['Elements']); coords=parse_coords(r['XYZ_Ang'])
            assert len(atoms)==len(coords)
            I=moments(atoms,coords)
            def num(col):
                v=r.get(col,float('nan'))
                return round(float(v),6) if math.isfinite(float(v)) else None
            result.append([
                int(r['Index']), str(r['SMILES']), *[round(float(x),5) for x in I],
                num('HOMO_LUMO_gap_au'), num('Dipole_debye'), num('Polarizability_bohr3'),
                len(atoms),
                ''.join({'H':'H','C':'C','N':'N','O':'O','F':'F'}[a] for a in atoms),
                [round(float(x),4) for x in coords.ravel()]
            ])
        except Exception as exc:
            errors.append((int(rowid),str(exc)))
    with open(output,'w',encoding='utf-8') as f:
        json.dump({'schema':'qm9-inertia-v1','units':'amu Angstrom^2','columns':['Index','SMILES','I1','I2','I3','gap','dipole','alpha','natoms','elements','xyz'], 'rows':result},f,separators=(',',':'))
    print(f'Wrote {len(result):,} molecules to {output}; skipped {len(errors)}')
    if errors: print('First errors:',errors[:5])

if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('--output',default='qm9_atlas.json'); args=ap.parse_args();run(args.output)
